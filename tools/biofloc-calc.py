#!/usr/bin/env python3
"""
Biofloc Carbon Dosing Calculator

Calculates how much carbon source to add based on:
- Daily feed input
- Feed protein content
- Target C:N ratio
- Carbon source type

Usage:
    python biofloc-calc.py              # Interactive mode
    python biofloc-calc.py --feed 100 --protein 35 --source molasses
"""

import sys
import argparse

# ─────────────────────────────────────────────────────────────────────
# Carbon Source Data
# ─────────────────────────────────────────────────────────────────────

CARBON_SOURCES = {
    "molasses": {
        "name": "Molasses",
        "carbon_pct": 40,   # ~40% carbon by weight
        "cn_ratio": 40,     # C:N ratio of the source itself
        "density_g_per_ml": 1.4,
        "cost_per_kg": 2.0,  # approximate USD
        "notes": "Most popular. Liquid, easy to dose. Available at feed stores.",
    },
    "wheat_flour": {
        "name": "Wheat Flour",
        "carbon_pct": 40,
        "cn_ratio": 40,
        "density_g_per_ml": None,
        "cost_per_kg": 1.0,
        "notes": "Cheap and available. Can cloud water temporarily.",
    },
    "rice_bran": {
        "name": "Rice Bran",
        "carbon_pct": 35,
        "cn_ratio": 35,
        "density_g_per_ml": None,
        "cost_per_kg": 0.8,
        "notes": "Common in Asia. Slightly lower carbon content.",
    },
    "sugar": {
        "name": "White Sugar (Sucrose)",
        "carbon_pct": 42,
        "cn_ratio": 500,  # virtually no nitrogen
        "density_g_per_ml": None,
        "cost_per_kg": 1.5,
        "notes": "Fast-acting. Pure carbon, no nitrogen contribution.",
    },
    "tapioca": {
        "name": "Tapioca Starch",
        "carbon_pct": 44,
        "cn_ratio": 45,
        "density_g_per_ml": None,
        "cost_per_kg": 1.2,
        "notes": "Good alternative to wheat flour. Common in SE Asia.",
    },
    "dextrose": {
        "name": "Dextrose",
        "carbon_pct": 40,
        "cn_ratio": 500,
        "density_g_per_ml": None,
        "cost_per_kg": 2.5,
        "notes": "Fast-acting like sugar. Easy to dissolve.",
    },
}

# ─────────────────────────────────────────────────────────────────────
# Core Calculation
# ─────────────────────────────────────────────────────────────────────

def calculate_carbon_dose(
    daily_feed_g: float,
    feed_protein_pct: float,
    target_cn_ratio: float,
    carbon_source_key: str,
) -> dict:
    """
    Calculate carbon source dosing for biofloc management.

    The science:
    1. Feed protein is ~16% nitrogen by weight (N = protein / 6.25)
    2. About 75% of feed nitrogen enters the water (25% retained by shrimp)
    3. To maintain target C:N, we need to add external carbon
    4. Carbon needed = Nitrogen_in_water × target_C:N - Carbon_already_in_feed

    Simplified approach used in practice:
    - N input to water = feed_g × (protein_pct/100) × 0.16 × 0.75
    - C needed = N_input × target_CN_ratio
    - C from feed ≈ feed_g × 0.05 (feed is ~5% available carbon for bacteria)
    - Additional C needed = C_needed - C_from_feed
    - Carbon source amount = Additional_C / (carbon_pct/100)
    """
    source = CARBON_SOURCES[carbon_source_key]

    # Nitrogen entering water from feed
    protein_g = daily_feed_g * (feed_protein_pct / 100)
    nitrogen_g = protein_g * 0.16  # protein is ~16% nitrogen
    n_in_water = nitrogen_g * 0.75  # ~75% enters water

    # Carbon needed for target C:N
    c_needed = n_in_water * target_cn_ratio

    # Carbon already available from feed decomposition
    c_from_feed = daily_feed_g * 0.05  # ~5% available C

    # Additional carbon needed
    additional_c = max(0, c_needed - c_from_feed)

    # Amount of carbon source
    source_carbon_pct = source["carbon_pct"] / 100
    source_g = additional_c / source_carbon_pct

    # Volume for liquid sources
    source_ml = None
    if source.get("density_g_per_ml"):
        source_ml = source_g / source["density_g_per_ml"]

    # Cost
    cost_per_day = source_g / 1000 * source["cost_per_kg"]
    cost_per_cycle = cost_per_day * 100  # ~100 day cycle

    return {
        "daily_feed_g": daily_feed_g,
        "feed_protein_pct": feed_protein_pct,
        "protein_g": protein_g,
        "nitrogen_g": nitrogen_g,
        "n_in_water_g": n_in_water,
        "c_needed_g": c_needed,
        "c_from_feed_g": c_from_feed,
        "additional_c_g": additional_c,
        "source_name": source["name"],
        "source_g": source_g,
        "source_ml": source_ml,
        "source_tablespoons": source_g / 15 if source_ml else source_g / 8,  # rough
        "cost_per_day": cost_per_day,
        "cost_per_cycle": cost_per_cycle,
        "notes": source["notes"],
    }


# ─────────────────────────────────────────────────────────────────────
# Display
# ─────────────────────────────────────────────────────────────────────

def print_result(r):
    print(f"\n{'='*55}")
    print(f"  Biofloc Carbon Dosing Calculation")
    print(f"{'='*55}")
    print(f"\n  INPUT")
    print(f"  Daily feed:         {r['daily_feed_g']:.1f} g")
    print(f"  Feed protein:       {r['feed_protein_pct']:.0f}%")
    print(f"  Protein input:      {r['protein_g']:.1f} g")
    print(f"  Nitrogen in water:  {r['n_in_water_g']:.2f} g")

    print(f"\n  CARBON BALANCE")
    print(f"  Carbon needed:      {r['c_needed_g']:.1f} g")
    print(f"  Carbon from feed:   {r['c_from_feed_g']:.1f} g")
    print(f"  Additional C:       {r['additional_c_g']:.1f} g")

    print(f"\n  DOSING ({r['source_name']})")
    print(f"  Amount:             {r['source_g']:.1f} g")
    if r['source_ml']:
        print(f"  Volume:             {r['source_ml']:.1f} ml")
    print(f"  (~{r['source_tablespoons']:.1f} tablespoons)")

    print(f"\n  COST")
    print(f"  Per day:            ${r['cost_per_day']:.3f}")
    print(f"  Per 100-day cycle:  ${r['cost_per_cycle']:.2f}")

    print(f"\n  NOTE: {r['notes']}")
    print(f"\n  TIPS:")
    print(f"  - Dissolve carbon source in tank water before adding")
    print(f"  - Add in 2-3 doses spread through the day")
    print(f"  - Monitor floc volume with Imhoff cone (target 10-15 ml/L)")
    print(f"  - If floc > 20 ml/L, reduce dosing or remove water")
    print(f"  - If floc < 5 ml/L, increase dosing slightly")
    print()


def print_comparison(daily_feed_g, feed_protein_pct, target_cn):
    print(f"\n{'='*70}")
    print(f"  Carbon Source Comparison ({daily_feed_g:.0f}g feed, {feed_protein_pct:.0f}% protein, C:N={target_cn:.0f})")
    print(f"{'='*70}")
    print(f"\n  {'Source':<18} {'Amount (g)':<12} {'$/day':<10} {'$/cycle':<10} Notes")
    print(f"  {'-'*66}")

    for key in CARBON_SOURCES:
        r = calculate_carbon_dose(daily_feed_g, feed_protein_pct, target_cn, key)
        print(f"  {r['source_name']:<18} {r['source_g']:<12.1f} ${r['cost_per_day']:<9.3f} ${r['cost_per_cycle']:<9.2f} {CARBON_SOURCES[key]['notes'][:30]}")
    print()


# ─────────────────────────────────────────────────────────────────────
# Interactive & CLI
# ─────────────────────────────────────────────────────────────────────

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


def interactive():
    print(f"\n{'='*55}")
    print(f"  Biofloc Carbon Dosing Calculator")
    print(f"{'='*55}\n")

    daily_feed = input_float("Daily feed amount (grams)", 100)
    protein = input_float("Feed protein content (%)", 35)
    target_cn = input_float("Target C:N ratio", 15)

    print("\n  Carbon sources:")
    keys = list(CARBON_SOURCES.keys())
    for i, k in enumerate(keys, 1):
        s = CARBON_SOURCES[k]
        print(f"    {i}. {s['name']} ({s['carbon_pct']}% C)")
    print(f"    {len(keys)+1}. Compare all")

    while True:
        raw = input("\n  Choice: ").strip()
        try:
            idx = int(raw)
            if 1 <= idx <= len(keys):
                result = calculate_carbon_dose(daily_feed, protein, target_cn, keys[idx-1])
                print_result(result)
                return
            elif idx == len(keys) + 1:
                print_comparison(daily_feed, protein, target_cn)
                return
        except ValueError:
            pass
        print(f"  Enter 1-{len(keys)+1}")


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--feed", type=float)
    parser.add_argument("--protein", type=float, default=35)
    parser.add_argument("--cn", type=float, default=15)
    parser.add_argument("--source", type=str, default=None)
    parser.add_argument("--compare", action="store_true")

    args, _ = parser.parse_known_args()

    if args.feed:
        if args.compare or not args.source:
            print_comparison(args.feed, args.protein, args.cn)
        elif args.source in CARBON_SOURCES:
            result = calculate_carbon_dose(args.feed, args.protein, args.cn, args.source)
            print_result(result)
        else:
            print(f"Unknown source: {args.source}")
            print(f"Options: {', '.join(CARBON_SOURCES.keys())}")
    else:
        interactive()


if __name__ == "__main__":
    main()
