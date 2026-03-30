# Water Quality Bible

> If you read one guide in this repo, read this one. Water quality kills more shrimp than disease, predators, and bad feed combined.

## Master Parameter Reference

<!--
  Quick-reference card. Print this and tape it next to your tanks.
-->

| Parameter | L. vannamei | M. rosenbergii | Neocaridina | Caridina |
|-----------|------------|----------------|-------------|---------|
| **Temperature** | 28-32°C | 28-31°C | 20-26°C | 20-23°C |
| **pH** | 7.5-8.5 | 7.0-8.5 | 6.8-7.5 | 6.0-6.5 |
| **Salinity (ppt)** | 15-25 | 0 | 0 | 0 |
| **GH (dGH)** | -- | 4-12 | 6-10 | 4-6 |
| **KH (dKH)** | -- | 2-8 | 2-6 | 0-1 |
| **TDS (ppm)** | -- | -- | 180-280 | 130-180 |
| **Dissolved O2** | >5 mg/L | >5 mg/L | >5 mg/L | >6 mg/L |
| **Ammonia (NH3)** | <0.1 | <0.1 | 0 | 0 |
| **Nitrite (NO2)** | <0.5 | <0.3 | 0 | 0 |
| **Nitrate (NO3)** | <20 | <20 | <10 | <5 |
| **Alkalinity** | 120-150 | 30-60 | 40-120 | 0-30 |
| **Calcium (mg/L)** | >200 | >50 | >40 | >30 |
| **Magnesium (mg/L)** | >50 | >20 | >10 | >5 |
| **Copper** | <0.01 | <0.01 | 0 | 0 |

---

## Understanding Each Parameter

### Temperature

Temperature controls metabolic rate, dissolved oxygen capacity, and disease susceptibility.

**Key facts**:
- Higher temp = faster growth BUT lower DO capacity AND faster disease progression
- Every 1°C increase reduces water's ability to hold oxygen by ~2%
- Shrimp stop feeding at species-specific low temps (vannamei: <22°C, rosenbergii: <20°C)
- Sudden changes (>2°C/hour) cause stress and mortality

**Managing temperature**:
- Heater: 5W per gallon rule (always use 2 for redundancy)
- Cooling: Fans (evaporative), shade, indoor placement
- Insulate tanks with foam board (R-10+) in cold climates

### pH

**What it is**: Measure of hydrogen ion concentration (acidity/alkalinity).

**Why it matters**:
- Affects ammonia toxicity (higher pH = more toxic NH3 vs harmless NH4+)
- Affects mineral availability
- Affects bacterial activity in biofilters
- Rapid pH changes are lethal

![pH vs Ammonia Toxicity](../../diagrams/ph-ammonia-toxicity.svg)

**pH and ammonia toxicity**:

| pH | % of Total Ammonia as Toxic NH3 (at 28°C) |
|----|-------------------------------------------|
| 7.0 | ~1% |
| 7.5 | ~3% |
| 8.0 | ~8% |
| 8.5 | ~22% |
| 9.0 | ~50% |

At pH 8.5, ammonia is **22x more toxic** than at pH 7.0. This is why pH matters.

**Raising pH**: Baking soda, crushed coral, limestone, aeration (drives off CO2)
**Lowering pH**: Active substrate (Caridina), peat, driftwood, CO2 injection

### The Nitrogen Cycle

![Nitrogen Cycle](../../diagrams/nitrogen-cycle.svg)

```
Fish/Shrimp Waste + Uneaten Feed
         ↓
    AMMONIA (NH3/NH4+)  ← TOXIC
         ↓  [Nitrosomonas bacteria]
    NITRITE (NO2-)      ← TOXIC
         ↓  [Nitrobacter bacteria]
    NITRATE (NO3-)      ← Low toxicity
         ↓
    Removed by: water changes, plants, denitrification
```

**In biofloc**: Heterotrophic bacteria shortcut this cycle by directly consuming ammonia (with added carbon) and converting it to bacterial biomass. Nitrite/nitrate levels stay lower.

**Cycling a new system**: Takes 2-6 weeks for bacteria to establish. During cycling:
- Ammonia rises first (week 1-2)
- Nitrite rises as ammonia drops (week 2-3)
- Nitrate rises as nitrite drops (week 3-6)
- Cycle is complete when ammonia = 0, nitrite = 0, nitrate present

### Dissolved Oxygen (DO)

**The silent killer.** Low DO kills faster than anything else.

| DO Level | Status |
|----------|--------|
| >6 mg/L | Excellent |
| 5-6 mg/L | Good |
| 4-5 mg/L | Stressed (reduce feeding) |
| 3-4 mg/L | Dangerous (emergency aeration) |
| <2 mg/L | Lethal (mass die-off in progress) |

**Factors that reduce DO**:
- High temperature (warm water holds less O2)
- High stocking density
- Overfeeding (decomposing feed consumes O2)
- High biofloc density
- Night time (no photosynthesis, bacteria still consuming)
- Power outage (aeration stops)

**The 4 AM danger zone**: In outdoor systems with algae, DO is lowest at 4-5 AM (all night respiration, no photosynthesis). This is when die-offs happen. Indoor systems with artificial aeration are more consistent.

### Alkalinity & Hardness

**KH (Carbonate Hardness)**: Measures bicarbonate/carbonate ions. Acts as pH buffer.
- Higher KH = more stable pH
- Biofloc consumes KH rapidly (bacteria produce acid)
- Low KH = pH crash risk

**GH (General Hardness)**: Measures calcium + magnesium ions. Essential for molting.
- Low GH = failed molts, soft shells, death
- Especially critical for Neocaridina and Caridina

**Alkalinity (CaCO3 equivalent)**: Related to KH but measured differently.
- 1 dKH ≈ 17.9 mg/L CaCO3
- Biofloc target: 120-150 mg/L CaCO3 (= ~7-8 dKH)

### Minerals (Ca, Mg, K)

The molting trinity. Shrimp build their exoskeleton from these.

**Calcium**: Primary shell component. Must be >200 mg/L for vannamei, >40 mg/L for ornamentals.
**Magnesium**: Assists calcium uptake. Ideal Ca:Mg ratio is roughly 3:1.
**Potassium**: Critical for osmoregulation, especially in low-salinity vannamei culture.

**Signs of mineral deficiency**:
- Failed molts (stuck in old shell)
- Soft shells that don't harden
- "White ring of death" (white band behind head in ornamentals = incomplete molt)
- Lethargy, reduced growth

---

## Testing Schedule

| Parameter | During Cycling | First Month | Stable System | Equipment |
|-----------|---------------|-------------|---------------|-----------|
| Temperature | 2x daily | Daily | Daily (glance) | Thermometer |
| pH | Daily | 3x/week | 1-2x/week | API kit or digital meter |
| Ammonia | Daily | 2-3x/week | 1x/week | API kit |
| Nitrite | Daily | 2-3x/week | 1x/week | API kit |
| Nitrate | 2x/week | 1x/week | 1x/week | API kit |
| Salinity | Daily | 2x/week | 1x/week | Refractometer |
| Alkalinity | -- | 2-3x/week (biofloc) | 2x/week | API KH kit |
| GH | -- | 1x/week | 1x/week | API GH kit |
| TDS | -- | 2x/week (ornamental) | 1x/week | TDS meter |
| DO | If meter available | Weekly | Weekly | DO meter |
| Floc volume | N/A | Daily (biofloc) | Every other day | Imhoff cone |

---

## Emergency Protocols

### Ammonia Spike (>1 mg/L)

1. **Stop feeding** immediately
2. **Water change**: 30-50% with clean, temperature/salinity-matched water
3. **Increase aeration** to maximum
4. **Add zeolite** to absorb ammonia (temporary, recharge in salt water)
5. **Add bacteria starter** to boost bio-filtration
6. **Test cause**: Overfeeding? Dead shrimp decomposing? Filter failure?
7. **Resume feeding** only when ammonia < 0.3 mg/L, at 50% normal rate

### pH Crash (<6.5 in vannamei/rosenbergii system)

1. **Add baking soda**: Emergency dose - 2g per 10L to quickly raise pH
2. **Check alkalinity**: It's probably depleted
3. **Increase aeration**: Drives off CO2, raises pH slightly
4. **Don't overshoot**: Raise pH no more than 0.5 units per hour
5. **Find root cause**: Usually depleted alkalinity from biofloc acid production

### Oxygen Crash

1. **Emergency aeration**: Splash water surface manually if no power
2. **Battery backup pump**: This is why you bought one
3. **Reduce biomass**: If possible, move some shrimp to a bucket with an air stone
4. **Don't feed**: Decomposing feed will consume more O2
5. **Partial water change**: Fresh water has more DO
6. **If power outage**: Use battery pump, open ice packs float in water (cold water holds more O2)

### Nitrite Spike (>2 mg/L)

1. **Add salt**: 1g/L of NaCl (table salt, non-iodized) blocks nitrite uptake through gills
2. **Water change**: 30-40%
3. **Reduce feeding** by 50%
4. **Check biofilter**: Is it working? Media clogged?
5. **Add bacteria starter**

---

## Test Equipment Recommendations

### Budget ($50-80)

| Item | Product | Cost |
|------|---------|------|
| Master test kit | API Saltwater Master Test Kit | $25-35 |
| Refractometer | Generic brix refractometer | $15-25 |
| Thermometer | Digital aquarium thermometer | $8-12 |
| **Total** | | **$48-72** |

### Mid-Range ($100-200)

Add to budget:

| Item | Product | Cost |
|------|---------|------|
| Digital pH meter | Apera PH20 | $40-55 |
| TDS meter | HM Digital TDS-3 | $10-15 |
| GH/KH test | API GH & KH Test Kit | $12-16 |
| Alkalinity test | API KH test or Salifert | $8-12 |
| Imhoff cone (biofloc) | 1000ml graduated | $15-25 |
| **Additional** | | **$85-123** |

### Professional ($300+)

Add to mid-range:

| Item | Product | Cost |
|------|---------|------|
| DO meter | Milwaukee MW600 | $80-120 |
| Calcium test | Salifert or Hanna | $12-20 |
| Magnesium test | Salifert | $12-18 |
| Digital refractometer | Milwaukee MA887 | $80-120 |
