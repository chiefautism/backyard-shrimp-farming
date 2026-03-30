# Biofloc Technology (BFT)

> Zero water exchange. Bacteria-powered filtration. Free supplemental protein. The backyard vannamei farmer's best friend.

## What is Biofloc?

Biofloc is a community of microorganisms - bacteria, protozoa, microalgae, and organic particles - that aggregate into visible "flocs" (clumps) in the water. In a biofloc system:

1. **Bacteria eat ammonia** (shrimp waste) when you provide a carbon source
2. **The floc IS your filter** - no external biofiltration needed
3. **Shrimp eat the floc** - it's 30-50% of their diet (free protein!)
4. **Minimal water exchange** - better biosecurity, less waste

This is the dominant method for backyard vannamei farming worldwide.

![Biofloc System Overview](../../diagrams/biofloc-system.svg)

## How it Works (The Science)

### The Carbon:Nitrogen Trick

In a normal aquarium, nitrifying bacteria (Nitrosomonas, Nitrobacter) slowly convert ammonia -> nitrite -> nitrate. This is slow and produces nitrate you have to remove with water changes.

In biofloc, **heterotrophic bacteria** are turbo-charged by adding external carbon. These bacteria:
- Grow 10x faster than nitrifying bacteria
- Consume ammonia directly, converting it into bacterial biomass
- Need a C:N ratio of **15-20:1** to thrive
- The resulting bacterial colonies (+ protozoa that graze on them) form the visible "floc"

### The Floc Community

- **Layer 1**: Heterotrophic bacteria (Bacillus, Lactobacillus, etc.) - the workhorses
- **Layer 2**: Protozoa (ciliates, flagellates) - graze on bacteria, part of the food chain
- **Layer 3**: Microalgae (if light is present) - photosynthetic addition
- **Layer 4**: Organic particles, dead cells, detritus - bound together by bacterial EPS (exopolysaccharides)

The whole thing forms clumps (flocs) 0.1-3mm in size that shrimp actively graze on.

---

## Setting Up a Biofloc System

### Equipment Shopping List

| Item | Specific Product | Cost | Notes |
|------|-----------------|------|-------|
| Tank | IBC tote 275 gal (used) | $50-150 | Cut top, paint exterior dark |
| Air pump | Hakko HK-40L (for 2-4 tanks) | $140-170 | Linear, reliable, quiet |
| Air stones | 4" ceramic (4 per tank) | $2-5 each | Replace every 6 months |
| Air tubing | Silicone, 25ft roll | $8-15 | Better than vinyl |
| Heater | 2x 300W submersible | $30-50 total | Redundancy! |
| Thermometer | Digital with probe | $10-15 | |
| Salt | Instant Ocean or similar | $15-40 per bag | If doing saltwater |
| Test kit | API Saltwater Master | $25-35 | pH, ammonia, nitrite, nitrate |
| Refractometer | Standard | $15-25 | Salinity measurement |
| Imhoff cone | 1000ml graduated | $15-25 | Floc volume measurement |
| Carbon source | Molasses (1 gallon) | $8-15 | Feed stores or Amazon |
| Bacteria starter | Commercial probiotic | $15-30 | Optional but speeds startup |
| Backup air pump | Battery-powered | $15-25 | LIFE INSURANCE |
| Battery backup | UPS 350-500VA | $30-60 | For main pump during power outage |
| **Total** | | **$350-650** | For first tank |

### Step-by-Step Setup

![IBC Tote Setup Diagram](../../diagrams/ibc-tote-setup.svg)

#### Step 1: Tank Preparation (Day 1)

1. **Clean IBC tote** with freshwater (no soap, no chemicals)
2. **Cut top** with reciprocating saw or angle grinder (leave frame for rigidity)
3. **Paint exterior** dark color (black spray paint) - reduces algae, reduces shrimp stress
4. **Position** on level surface with good drainage
5. **Consider shade** - partial shade reduces algae and overheating

#### Step 2: Water (Day 1-2)

1. **Fill** with dechlorinated freshwater (let stand 24h or use dechlorinator)
2. **Add salt** if doing saltwater culture:
   - Target 15 ppt: ~15 kg salt per 1000L (~40 lbs per 275 gal)
   - Mix thoroughly, let dissolve 24 hours
   - Verify with refractometer
3. **Add minerals** if doing low-salinity/freshwater:
   - Calcium chloride: 0.7g/L for 200 mg/L Ca
   - Epsom salt: 0.5g/L for 50 mg/L Mg
   - Potassium chloride: 0.2g/L for 100 mg/L K

#### Step 3: Aeration (Day 1)

1. **Install air stones** at bottom: 4 stones per IBC, evenly spaced
2. **Connect to air pump** with silicone tubing
3. **Turn on** - water should visibly "roll" with vigorous circulation
4. **Test DO** if you have a meter: target >5 mg/L
5. Aeration runs **24/7 from this point forward. No exceptions.**

#### Step 4: Seed the Biofloc (Day 2-3)

**Option A: From existing biofloc (best)**
- Get 10-20L of mature biofloc water from an existing system
- Add to your tank
- Floc establishes in 3-5 days

**Option B: From scratch**
1. Add bacteria starter (commercial probiotic or pond bacteria)
2. Add first carbon dose: 2ml molasses per 10L of water
3. Add ammonia source: 1-2g of shrimp feed per 100L (to decompose and provide N)
4. Wait 7-14 days for floc to develop

#### Step 5: Carbon Source Management

This is the core skill of biofloc farming.

| Carbon Source | Carbon % | Dosing Rate (per g of feed) | Cost/kg | Pros | Cons |
|--------------|----------|---------------------------|---------|------|------|
| **Molasses** | 40% | 0.5-1 ml | $2 | Easy to dose (liquid), available | Sticky, fermenting smell |
| **Wheat flour** | 40% | 0.5-0.7 g | $1 | Cheap, everywhere | Clouds water temporarily |
| **Rice bran** | 35% | 0.7-0.9 g | $0.80 | Cheap, adds some nutrition | Slightly lower carbon |
| **Sugar** | 42% | 0.4-0.6 g | $1.50 | Fast-acting, precise | No nitrogen contribution |
| **Tapioca starch** | 44% | 0.4-0.6 g | $1.20 | Good in SE Asia | |
| **Dextrose** | 40% | 0.4-0.6 g | $2.50 | Dissolves easily | More expensive |

**The Formula**:

```
Nitrogen entering water = Daily feed (g) × Protein% × 0.16 × 0.75
Carbon needed = Nitrogen × Target C:N ratio (15-20)
Carbon from feed ≈ Daily feed (g) × 0.05
Additional carbon needed = Carbon needed - Carbon from feed
Carbon source amount = Additional carbon / Carbon% of source
```

**Quick Rule of Thumb**: Add carbon source equal to 50-60% of daily feed weight (for molasses or wheat flour).

Use the [Biofloc Calculator](../../tools/biofloc-calc.py) for exact calculations.

#### Step 6: Monitor Floc Development (Day 3-14)

**Imhoff Cone Method**:
1. Fill 1L Imhoff cone with tank water
2. Let settle for 15-20 minutes
3. Read settled volume at bottom
4. **Target: 10-15 ml/L**

| Floc Volume | Status | Action |
|-------------|--------|--------|
| 0-5 ml/L | Low / developing | Increase carbon dosing, check aeration |
| 5-10 ml/L | Building | Continue current protocol |
| 10-15 ml/L | Ideal | Maintain |
| 15-20 ml/L | High | Reduce carbon dosing slightly |
| >20 ml/L | Too high | Remove water (partial exchange), reduce carbon |

**Healthy floc looks like**: Brown/tan color, earthy smell (not foul), visible particles throughout water column.

**Unhealthy signs**: Black color (anaerobic), rotten egg smell (H2S), foam that doesn't dissipate, green water only (algae dominant, not bacterial).

#### Step 7: Stocking (Day 14-21)

Stock shrimp when:
- Ammonia < 0.5 mg/L (ideally < 0.1)
- Nitrite < 1.0 mg/L (ideally < 0.5)
- Floc volume 5-10 ml/L (doesn't need to be perfect yet)
- Temperature stable at 28-32°C
- Salinity at target

---

## Daily Management Protocol

### Morning Routine (10 min)

- [ ] Check aeration is running (MOST IMPORTANT)
- [ ] Check temperature
- [ ] Visual inspection (shrimp behavior, water color, any dead shrimp)
- [ ] First feeding (use feed tray)

### Midday

- [ ] Check feed tray (should be cleared within 2 hours)
- [ ] Adjust next feeding amount based on consumption
- [ ] Add carbon source dose #1

### Afternoon

- [ ] Second feeding
- [ ] Measure floc volume (Imhoff cone) - daily during first month, every other day after
- [ ] Add carbon source dose #2

### Evening

- [ ] Third feeding (if applicable for growth stage)
- [ ] Quick visual check

### Weekly

- [ ] Full water parameter test (pH, ammonia, nitrite, nitrate)
- [ ] Alkalinity test (CRITICAL - see below)
- [ ] Salinity check (refractometer)
- [ ] Record all data in logbook

---

## Alkalinity Management (THE MOST UNDERRATED SKILL)

**Biofloc consumes alkalinity.** The heterotrophic bacteria that make biofloc work produce acid as a byproduct. This steadily lowers alkalinity and eventually causes pH to crash.

### Why It Matters

- Low alkalinity = unstable pH
- pH crash = mass die-off (can happen overnight)
- The more feed (= more bacteria = more acid), the faster alkalinity drops

### Target: 120-150 mg/L CaCO3

### Testing Frequency

- First month: 2-3x per week
- After stable: 2x per week minimum
- If alkalinity drops below 100: test daily until corrected

### Dosing Baking Soda (Sodium Bicarbonate)

| Situation | Dose | Notes |
|-----------|------|-------|
| Maintenance | 1g per 10L raises ~12 mg/L CaCO3 | |
| Correction | Max 30 mg/L CaCO3 increase per day | Don't shock the system |
| Emergency (pH crash) | Up to 50 mg/L CaCO3 at once | Better to overshoot than lose stock |

**How to apply**: Dissolve baking soda in bucket of tank water first. Never add dry powder directly. Pour slowly into high-flow area.

### Alternative Products

| Product | Effect | When to Use |
|---------|--------|------------|
| Baking soda (NaHCO3) | Raises alkalinity + pH | Primary choice |
| Agricultural lime (CaCO3) | Raises alkalinity + calcium | Good dual-purpose |
| Dolomite (CaCO3 + MgCO3) | Raises alkalinity + Ca + Mg | If Mg is also low |
| Hydrated lime (Ca(OH)2) | Rapid pH/alkalinity increase | Emergency only (caustic) |

---

## Troubleshooting

### Floc Too High (>20 ml/L)

**Symptoms**: Very cloudy water, shrimp may be stressed, DO can drop.

**Causes**: Too much carbon dosing, overfeeding, insufficient water exchange.

**Immediate Actions**:
1. Stop carbon dosing for 24-48 hours
2. Remove 20-30% water, replace with clean saltwater
3. Increase aeration if possible
4. Reduce feeding by 30%

### Floc Too Low (<5 ml/L)

**Causes**: Insufficient carbon, inadequate aeration, water too clean.

**Actions**:
1. Increase carbon dose by 25-50%
2. Verify aeration is adequate
3. Add small amount of feed as nitrogen source
4. Be patient - floc takes days to build

### Floc Crash (Sudden Collapse)

**Symptoms**: Water suddenly clears, ammonia spikes, shrimp stressed.

**Causes**: Power outage killed bacteria, chemical contamination, pH crash, cold snap.

**Emergency Protocol**:
1. Test ammonia immediately
2. If ammonia > 1 mg/L: partial water change (30-50%)
3. Increase aeration to maximum
4. Add bacteria starter / probiotic
5. Resume carbon dosing
6. Reduce or stop feeding for 24-48 hours
7. Re-establish floc over following week

### Foul Smell (Rotten Eggs)

**Cause**: Anaerobic zones (dead spots without oxygen). Hydrogen sulfide production.

**This is dangerous** - H2S is toxic to shrimp even at low levels.

**Actions**:
1. Increase aeration immediately
2. Add air stone to dead spots
3. Stir up any settled sludge (to expose to oxygen)
4. Partial water change if severe
5. Check that bottom of tank isn't accumulating sludge

### Foam on Surface

- **Thin white foam**: Normal in early stages, protein skimming. Usually harmless.
- **Thick persistent foam**: Overfeeding, dying bacteria, or chemical contamination. Reduce feed, check parameters.
- **Brown/green foam**: Algae bloom. Increase shade, reduce light.

---

## Scaling Up

### From 1 Tank to Multiple

| Scale | Tanks | Aeration | Management Time | Notes |
|-------|-------|----------|----------------|-------|
| Learning | 1 | Individual pump | 30 min/day | Focus on fundamentals |
| Hobby | 2-4 | Hakko HK-40L shared | 45-60 min/day | Can share water source |
| Side business | 4-8 | Hakko HK-80L or 2x HK-40L | 1-2 hours/day | Need organized routine |
| Serious | 8-16 | Regenerative blower | 2-3 hours/day | Need dedicated space |

### Tips for Scaling

1. **Stagger cycles** - don't start all tanks at once. Start one, learn, then add.
2. **Shared plumbing** - water mixing/preparation tank saves time
3. **Consistent routine** - same order, same checks, every day
4. **Record everything** - spreadsheet: date, tank, parameters, feed, carbon, notes
5. **Batch water prep** - make saltwater in bulk in a separate mixing tank
6. **Backup systems** - the more tanks, the more critical backup aeration becomes
