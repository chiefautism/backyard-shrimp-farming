#!/usr/bin/env python3
"""
Backyard Shrimp Farming - Water Quality & Dosing Calculator

Usage:
    python water-calc.py                  # Interactive mode
    python water-calc.py salt             # Salt mixing calculator
    python water-calc.py stock            # Stocking density calculator
    python water-calc.py feed             # Feed rate calculator
    python water-calc.py alkalinity       # Alkalinity dosing calculator
    python water-calc.py minerals         # Mineral dosing calculator
    python water-calc.py water-change     # Water change calculator
    python water-calc.py params           # Parameter reference card
"""

import sys
import math

# ─────────────────────────────────────────────────────────────────────
# Constants & Reference Data
# ─────────────────────────────────────────────────────────────────────

SPECIES = {
    "vannamei": {
        "name": "L. vannamei (Pacific White Shrimp)",
        "temp_min": 26, "temp_max": 33, "temp_optimal_min": 28, "temp_optimal_max": 32,
        "ph_min": 7.0, "ph_max": 9.0, "ph_optimal_min": 7.5, "ph_optimal_max": 8.5,
        "salinity_min": 0.5, "salinity_max": 40, "salinity_optimal_min": 15, "salinity_optimal_max": 25,
        "do_min": 4.0, "do_optimal": 5.0,
        "ammonia_max": 0.1, "nitrite_max": 1.0, "nitrate_max": 50,
        "alkalinity_min": 120, "alkalinity_max": 150,
        "calcium_min": 200, "magnesium_min": 50, "potassium_min": 100,
    },
    "rosenbergii": {
        "name": "M. rosenbergii (Giant Freshwater Prawn)",
        "temp_min": 24, "temp_max": 33, "temp_optimal_min": 26, "temp_optimal_max": 31,
        "ph_min": 7.0, "ph_max": 8.5, "ph_optimal_min": 7.0, "ph_optimal_max": 8.5,
        "salinity_min": 0, "salinity_max": 5, "salinity_optimal_min": 0, "salinity_optimal_max": 3,
        "do_min": 3.0, "do_optimal": 5.0,
        "ammonia_max": 0.1, "nitrite_max": 0.5, "nitrate_max": 40,
        "alkalinity_min": 20, "alkalinity_max": 60,
        "calcium_min": 50, "magnesium_min": 20, "potassium_min": 30,
    },
    "neocaridina": {
        "name": "Neocaridina davidi (Cherry Shrimp)",
        "temp_min": 15, "temp_max": 30, "temp_optimal_min": 20, "temp_optimal_max": 26,
        "ph_min": 6.5, "ph_max": 8.0, "ph_optimal_min": 6.8, "ph_optimal_max": 7.5,
        "salinity_min": 0, "salinity_max": 0, "salinity_optimal_min": 0, "salinity_optimal_max": 0,
        "do_min": 4.0, "do_optimal": 6.0,
        "ammonia_max": 0.0, "nitrite_max": 0.0, "nitrate_max": 20,
        "alkalinity_min": 40, "alkalinity_max": 120,
        "calcium_min": 40, "magnesium_min": 10, "potassium_min": 5,
    },
    "caridina": {
        "name": "Caridina cantonensis (Crystal/Bee Shrimp)",
        "temp_min": 16, "temp_max": 26, "temp_optimal_min": 20, "temp_optimal_max": 24,
        "ph_min": 5.4, "ph_max": 7.0, "ph_optimal_min": 5.8, "ph_optimal_max": 6.8,
        "salinity_min": 0, "salinity_max": 0, "salinity_optimal_min": 0, "salinity_optimal_max": 0,
        "do_min": 5.0, "do_optimal": 7.0,
        "ammonia_max": 0.0, "nitrite_max": 0.0, "nitrate_max": 10,
        "alkalinity_min": 0, "alkalinity_max": 30,
        "calcium_min": 30, "magnesium_min": 5, "potassium_min": 3,
    },
}

# Grams of salt per liter to achieve 1 ppt salinity
GRAMS_SALT_PER_LITER_PER_PPT = 1.0

# Baking soda: ~1g per liter raises alkalinity by ~12 mg/L CaCO3
BAKING_SODA_ALK_FACTOR = 12.0  # mg/L CaCO3 per g/L of NaHCO3

# CaCl2: ~1g per liter raises calcium by ~272 mg/L (as Ca)
CACL2_CA_FACTOR = 272.0

# Epsom salt (MgSO4·7H2O): ~1g per liter raises Mg by ~99 mg/L
EPSOM_MG_FACTOR = 99.0

# KCl: ~1g per liter raises K by ~524 mg/L
KCL_K_FACTOR = 524.0


def liters_from_gallons(gal):
    return gal * 3.78541


def gallons_from_liters(L):
    return L / 3.78541


def input_float(prompt, default=None):
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"{prompt}{suffix}: ").strip()
        if raw == "" and default is not None:
            return float(default)
        try:
            return float(raw)
        except ValueError:
            print("  Please enter a number.")


def input_choice(prompt, options):
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        raw = input("Choice: ").strip()
        try:
            idx = int(raw)
            if 1 <= idx <= len(options):
                return idx - 1
        except ValueError:
            pass
        print(f"  Please enter 1-{len(options)}.")


def header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


# ─────────────────────────────────────────────────────────────────────
# Calculators
# ─────────────────────────────────────────────────────────────────────

def salt_calculator():
    header("Salt Mixing Calculator")
    volume_gal = input_float("Tank volume (gallons)")
    volume_L = liters_from_gallons(volume_gal)
    target_ppt = input_float("Target salinity (ppt)", 15)
    current_ppt = input_float("Current salinity (ppt)", 0)

    delta = target_ppt - current_ppt
    if delta <= 0:
        print("\n  Current salinity is already at or above target.")
        return

    grams_needed = delta * GRAMS_SALT_PER_LITER_PER_PPT * volume_L
    lbs_needed = grams_needed / 453.592
    cups_approx = grams_needed / 273  # ~273g marine salt per cup

    print(f"\n  Tank volume:      {volume_gal:.0f} gal ({volume_L:.0f} L)")
    print(f"  Salinity change:  {current_ppt:.1f} -> {target_ppt:.1f} ppt")
    print(f"  Salt needed:      {grams_needed:.0f} g ({lbs_needed:.1f} lbs, ~{cups_approx:.1f} cups)")
    print(f"\n  Tip: Add salt gradually over several hours. Mix well.")
    print(f"  Tip: Use a refractometer to verify, not just calculations.")


def stocking_calculator():
    header("Stocking Density Calculator")

    species_keys = list(SPECIES.keys())
    species_names = [SPECIES[k]["name"] for k in species_keys]
    idx = input_choice("Select species:", species_names)
    species = species_keys[idx]

    volume_gal = input_float("Tank volume (gallons)")
    volume_L = liters_from_gallons(volume_gal)
    volume_m3 = volume_L / 1000

    if species == "vannamei":
        densities = [
            ("Conservative (beginner)", 50, 100),
            ("Moderate (experienced)", 100, 200),
            ("Intensive (expert)", 200, 300),
        ]
        print(f"\n  Tank: {volume_gal:.0f} gal ({volume_L:.0f} L, {volume_m3:.2f} m³)")
        print(f"\n  Recommended stocking for {SPECIES[species]['name']}:")
        for label, low, high in densities:
            n_low = int(low * volume_m3)
            n_high = int(high * volume_m3)
            print(f"    {label}: {n_low}-{n_high} shrimp")
    elif species == "rosenbergii":
        # Rosenbergii uses per m² (they're bottom dwellers)
        # Approximate: assume tank is ~0.5m deep for area calc
        area_m2 = volume_m3 / 0.5
        densities = [
            ("Low density", 5, 10),
            ("Medium density", 10, 15),
        ]
        print(f"\n  Tank: {volume_gal:.0f} gal ({volume_L:.0f} L)")
        print(f"  Estimated bottom area: ~{area_m2:.1f} m² (assuming 0.5m depth)")
        print(f"\n  Recommended stocking for {SPECIES[species]['name']}:")
        for label, low, high in densities:
            n_low = int(low * area_m2)
            n_high = int(high * area_m2)
            print(f"    {label}: {n_low}-{n_high} prawns")
    else:
        # Ornamental - per gallon
        densities = [
            ("Breeding colony", 2, 5),
            ("Display tank", 1, 3),
        ]
        print(f"\n  Tank: {volume_gal:.0f} gal ({volume_L:.0f} L)")
        print(f"\n  Recommended stocking for {SPECIES[species]['name']}:")
        for label, low, high in densities:
            n_low = int(low * volume_gal)
            n_high = int(high * volume_gal)
            print(f"    {label}: {n_low}-{n_high} shrimp")

    print(f"\n  Start conservative. Increase density only with experience.")


def feed_calculator():
    header("Feed Rate Calculator")

    volume_gal = input_float("Tank volume (gallons)")
    num_shrimp = input_float("Number of shrimp")
    avg_weight_g = input_float("Average shrimp weight (grams)", 5)
    total_biomass_g = num_shrimp * avg_weight_g
    total_biomass_kg = total_biomass_g / 1000

    if avg_weight_g < 0.5:
        feed_pct = 10.0
        feedings = 6
        stage = "Post-larval"
        protein = "38-42%"
    elif avg_weight_g < 2:
        feed_pct = 8.0
        feedings = 5
        stage = "Early juvenile"
        protein = "38-40%"
    elif avg_weight_g < 5:
        feed_pct = 5.0
        feedings = 4
        stage = "Juvenile"
        protein = "35-38%"
    elif avg_weight_g < 10:
        feed_pct = 4.0
        feedings = 3
        stage = "Sub-adult"
        protein = "32-35%"
    elif avg_weight_g < 20:
        feed_pct = 3.0
        feedings = 3
        stage = "Growing"
        protein = "30-35%"
    else:
        feed_pct = 2.5
        feedings = 2
        stage = "Adult/finishing"
        protein = "30-32%"

    daily_feed_g = total_biomass_g * (feed_pct / 100)
    per_feeding_g = daily_feed_g / feedings

    print(f"\n  Shrimp count:     {num_shrimp:.0f}")
    print(f"  Avg weight:       {avg_weight_g:.1f} g")
    print(f"  Total biomass:    {total_biomass_g:.0f} g ({total_biomass_kg:.2f} kg)")
    print(f"  Growth stage:     {stage}")
    print(f"  Feed protein:     {protein}")
    print(f"  Feed rate:        {feed_pct:.1f}% of body weight/day")
    print(f"  Daily feed:       {daily_feed_g:.1f} g")
    print(f"  Per feeding:      {per_feeding_g:.1f} g ({feedings}x/day)")
    print(f"\n  Tip: Use feed trays to monitor actual consumption.")
    print(f"  Tip: Reduce by 30-50% if using biofloc (floc is food too).")


def alkalinity_calculator():
    header("Alkalinity Dosing Calculator (Baking Soda)")

    volume_gal = input_float("Tank volume (gallons)")
    volume_L = liters_from_gallons(volume_gal)
    current_alk = input_float("Current alkalinity (mg/L CaCO3)", 80)
    target_alk = input_float("Target alkalinity (mg/L CaCO3)", 140)

    delta = target_alk - current_alk
    if delta <= 0:
        print("\n  Alkalinity is already at or above target.")
        return

    # g/L needed = delta / BAKING_SODA_ALK_FACTOR
    g_per_L = delta / BAKING_SODA_ALK_FACTOR
    total_g = g_per_L * volume_L
    teaspoons = total_g / 4.6  # ~4.6g baking soda per teaspoon

    print(f"\n  Tank volume:      {volume_gal:.0f} gal ({volume_L:.0f} L)")
    print(f"  Alkalinity raise: {current_alk:.0f} -> {target_alk:.0f} mg/L CaCO3")
    print(f"  Baking soda:      {total_g:.1f} g (~{teaspoons:.1f} teaspoons)")
    print(f"\n  WARNING: Do not raise alkalinity by more than 30 mg/L per day.")
    if delta > 30:
        daily_g = (30 / BAKING_SODA_ALK_FACTOR) * volume_L
        daily_tsp = daily_g / 4.6
        days = math.ceil(delta / 30)
        print(f"  Recommended: {daily_g:.1f} g/day ({daily_tsp:.1f} tsp/day) over {days} days.")
    print(f"\n  Dissolve in tank water before adding. Never add dry powder directly.")


def mineral_calculator():
    header("Mineral Dosing Calculator")

    volume_gal = input_float("Tank volume (gallons)")
    volume_L = liters_from_gallons(volume_gal)

    print("\n  Which mineral to dose?")
    mineral = input_choice("", ["Calcium (CaCl2)", "Magnesium (Epsom Salt / MgSO4)", "Potassium (KCl)"])

    if mineral == 0:
        current = input_float("Current calcium (mg/L)", 100)
        target = input_float("Target calcium (mg/L)", 250)
        delta = target - current
        if delta <= 0:
            print("\n  Already at or above target.")
            return
        g_per_L = delta / CACL2_CA_FACTOR
        total_g = g_per_L * volume_L
        print(f"\n  CaCl2 needed:     {total_g:.1f} g")
        print(f"  Dissolve first, add slowly over 24 hours.")

    elif mineral == 1:
        current = input_float("Current magnesium (mg/L)", 20)
        target = input_float("Target magnesium (mg/L)", 60)
        delta = target - current
        if delta <= 0:
            print("\n  Already at or above target.")
            return
        g_per_L = delta / EPSOM_MG_FACTOR
        total_g = g_per_L * volume_L
        teaspoons = total_g / 5  # ~5g per teaspoon
        print(f"\n  Epsom salt needed: {total_g:.1f} g (~{teaspoons:.1f} teaspoons)")
        print(f"  Dissolve first, add slowly.")

    elif mineral == 2:
        current = input_float("Current potassium (mg/L)", 50)
        target = input_float("Target potassium (mg/L)", 120)
        delta = target - current
        if delta <= 0:
            print("\n  Already at or above target.")
            return
        g_per_L = delta / KCL_K_FACTOR
        total_g = g_per_L * volume_L
        print(f"\n  KCl needed:       {total_g:.1f} g")
        print(f"  Dissolve first, add slowly over 24 hours.")


def water_change_calculator():
    header("Water Change Calculator")

    volume_gal = input_float("Tank volume (gallons)")
    volume_L = liters_from_gallons(volume_gal)
    pct = input_float("Water change percentage", 20)
    change_L = volume_L * (pct / 100)
    change_gal = gallons_from_liters(change_L)

    current_param = input_float("Current parameter value (e.g., nitrate mg/L)", 40)
    new_water_param = input_float("Replacement water parameter value", 0)

    after = current_param * (1 - pct/100) + new_water_param * (pct/100)

    print(f"\n  Water to remove:  {change_gal:.1f} gal ({change_L:.0f} L)")
    print(f"  Parameter before: {current_param:.1f}")
    print(f"  Parameter after:  {after:.1f}")
    print(f"\n  Tip: Match temperature within 1°C and salinity within 2 ppt.")
    print(f"  Tip: Dechlorinate replacement water before adding.")


def params_reference():
    header("Water Parameter Quick Reference")

    print("  Parameter          | Vannamei     | Rosenbergii  | Neocaridina  | Caridina")
    print("  " + "-"*85)
    rows = [
        ("Temperature (°C)",  "temp_optimal_min", "temp_optimal_max"),
        ("pH",                "ph_optimal_min",   "ph_optimal_max"),
        ("Salinity (ppt)",    "salinity_optimal_min", "salinity_optimal_max"),
        ("DO min (mg/L)",     "do_optimal",       None),
        ("Ammonia max",       "ammonia_max",      None),
        ("Nitrite max",       "nitrite_max",      None),
        ("Nitrate max",       "nitrate_max",      None),
        ("Alkalinity min",    "alkalinity_min",   "alkalinity_max"),
    ]

    for label, key_low, key_high in rows:
        parts = []
        for sp in ["vannamei", "rosenbergii", "neocaridina", "caridina"]:
            d = SPECIES[sp]
            if key_high and key_high in d:
                parts.append(f"{d[key_low]}-{d[key_high]}")
            else:
                val = d[key_low]
                parts.append(f"{val}" if val > 0 else "0")
        line = f"  {label:<20} | {parts[0]:<12} | {parts[1]:<12} | {parts[2]:<12} | {parts[3]}"
        print(line)

    print(f"\n  Units: Temperature=°C, Salinity=ppt, DO/Ammonia/Nitrite/Nitrate=mg/L")
    print(f"  Alkalinity=mg/L CaCO3")


def interactive_menu():
    header("Backyard Shrimp Farming Calculator")
    print("  Tools available:\n")
    options = [
        "Salt mixing calculator",
        "Stocking density calculator",
        "Feed rate calculator",
        "Alkalinity dosing (baking soda)",
        "Mineral dosing (Ca, Mg, K)",
        "Water change calculator",
        "Parameter reference card",
        "Exit",
    ]
    funcs = [
        salt_calculator,
        stocking_calculator,
        feed_calculator,
        alkalinity_calculator,
        mineral_calculator,
        water_change_calculator,
        params_reference,
    ]

    while True:
        idx = input_choice("\nSelect a tool:", options)
        if idx == len(options) - 1:
            print("\n  Happy shrimp farming!\n")
            break
        funcs[idx]()


# ─────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────

def main():
    commands = {
        "salt": salt_calculator,
        "stock": stocking_calculator,
        "feed": feed_calculator,
        "alkalinity": alkalinity_calculator,
        "minerals": mineral_calculator,
        "water-change": water_change_calculator,
        "params": params_reference,
    }

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in commands:
            commands[cmd]()
        elif cmd in ("-h", "--help", "help"):
            print(__doc__)
        else:
            print(f"Unknown command: {cmd}")
            print(__doc__)
    else:
        interactive_menu()


if __name__ == "__main__":
    main()
