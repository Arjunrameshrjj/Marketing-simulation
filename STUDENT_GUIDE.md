# 🎯 Student Quick Start Guide

Welcome to the Adobe Creative Cloud Marketing Budget Simulation!

## What You'll Learn

- How to allocate marketing budgets across customer lifecycle stages
- The trade-off between short-term results and long-term investment
- Why customer retention matters as much as acquisition
- How to plan strategically across multiple quarters

## The Challenge

**Your Mission:** Maximize Annual Recurring Revenue (ARR) over 8 quarters

**Constraints:**
- **2021:** $250M budget per quarter → Target: $500M ARR per quarter
- **2022:** $300M budget per quarter → Target: $625M ARR per quarter

## Getting Started

### Installation (5 minutes)

1. **Download the simulation files** to your computer

2. **Open Terminal** (Mac/Linux) or **Command Prompt** (Windows)

3. **Navigate to the folder:**
   ```bash
   cd path/to/marketing_simulation
   ```

4. **Run the simulation:**
   ```bash
   ./run.sh
   ```
   
   Or if that doesn't work:
   ```bash
   streamlit run app.py
   ```

5. **Your browser will open automatically** to http://localhost:8501

## Understanding the 5 Phases (DDOM)

Think of it like a funnel:

```
🌐 DISCOVER → 🔍 TRY → 💰 BUY → 🎮 USE → 🔄 RENEW
```

### 1. 🌐 **Discover** (Drive Traffic)
- **Variable:** Awareness Marketing (ads, campaigns)
- **Fixed:** Landing Page Optimization
- **Goal:** Get people to your website

### 2. 🔍 **Try** (Get Trials)
- **Variable:** Consideration Marketing (emails, social)
- **Fixed:** Recommendation Engine (AI matching)
- **Goal:** Convert visitors to free trials

### 3. 💰 **Buy** (Make Sales)
- **Variable:** Performance Marketing (retargeting, SEM)
- **Fixed:** E-Commerce Optimization
- **Goal:** Convert trials to paying customers
- **Impact:** Creates Gross ARR

### 4. 🎮 **Use** (Engage Customers)
- **Variable:** Engagement Marketing (tutorials, tips)
- **Fixed:** Product Engagement (onboarding, features)
- **Goal:** Keep customers active and happy

### 5. 🔄 **Renew** (Reduce Churn)
- **Variable:** Save Offers (discounts to retain)
- **Fixed:** Payment Processing (reduce failed payments)
- **Goal:** Prevent customers from canceling
- **Impact:** Reduces Cancel ARR

## The Key Formula

```
Net-New ARR = Gross New ARR - Cancel ARR
```

- **Gross ARR:** Revenue from new customer orders (Buy phase)
- **Cancel ARR:** Revenue lost from customers who left (Renew phase)
- **Your goal:** Maximize Net-New ARR!

## Variable vs. Fixed Spending

### **Variable Spend** = Short-term 💨
- Results **THIS quarter**
- Like buying ads today → sales today
- Immediate impact

### **Fixed Spend** = Long-term 🌱
- Results **NEXT quarter** (and beyond)
- Like planting seeds → harvest later
- Compounds over time

**Example:**
- Q1: Spend $10M on Landing Page Optimization (fixed)
- Q2: Your conversion rate improves → more trials with same traffic!
- Q3: Still benefiting from Q1 investment!

## Quick Strategy Tips

### ✅ **DO:**
1. **Start with balance** (20% each phase is a good starting point)
2. **Invest in fixed early** (Q1-Q2 of each year)
3. **Keep Renew at 5-10%** (don't let customers churn!)
4. **Be patient** (Q1 is always tough, Q2 gets better)
5. **Use all your budget** (every dollar counts)

### ❌ **DON'T:**
1. **Over-invest in one phase** (>45% on any single phase hurts)
2. **Ignore Renew** (<5% and churn will spike)
3. **Put 100% variable** (you need fixed for compounding)
4. **Change everything every quarter** (consistency compounds)
5. **Panic after Q1** (it's designed to be lower)

## What to Expect Each Quarter

### **Q1 Pattern:**
- Usually 80-85% of target
- This is NORMAL!
- You're building foundation
- Don't panic!

### **Q2 Pattern:**
- Big jump! (+15-25%)
- Q1 fixed investments kick in
- Expect to hit or exceed target
- Most exciting quarter

### **Q3-Q4 Pattern:**
- Plateau or slight improvement
- Optimization phase
- Stable results
- Fine-tune your strategy

## Your First Quarter (Step-by-Step)

**For Q1 2021, try this balanced approach:**

```
Total Budget: $250M

Discover:
  - Awareness Marketing: $46M
  - Landing Page Optimization: $6M
  - Total: $52M (20.8%)

Try:
  - Consideration Marketing: $34M
  - Recommendation Engine: $6M
  - Total: $40M (16%)

Buy:
  - Performance Marketing: $94M
  - E-Commerce Optimization: $6M
  - Total: $100M (40%)

Use:
  - Engagement Marketing: $36M
  - Product Engagement: $6M
  - Total: $42M (16.8%)

Renew:
  - Save Offers: $12M
  - Payment Processing: $4M
  - Total: $16M (6.4%)
```

**Expected Result:** ~$400-420M (80-84% of $500M target)

**Don't worry if it's not $500M!** Q1 is foundation-building.

## Tracking Your Progress

After each quarter, check:

1. **Net-New ARR** → Did you hit target?
2. **ROI** → Should be 1.5-2.0+
3. **Retention Rate** → Keep above 70%
4. **Trends** → Are metrics improving?

## Warning Signs

🚨 **Red Flags:**
- Net-New ARR dropping quarter-over-quarter
- Retention rate below 70%
- ROI below 1.5
- Cancel ARR increasing

**Fix:** 
- Check Renew budget (retention issue?)
- Review Buy budget (not enough new customers?)
- Look at phase balance

## Exit Criteria (Must Meet by Q4 2022)

By the end, you need:

- ✅ Website Visitors > 135M
- ✅ Free Trialists > 12.7M
- ✅ Orders > 1.5M
- ✅ Retention Rate > 70%

## Common Questions

**Q: Why is my Q1 result so low?**
A: It's designed that way! Q1 builds foundation, Q2 benefits from it.

**Q: Should I use more variable or fixed?**
A: Mix both! 80-90% variable, 10-20% fixed is typical.

**Q: Can I hit 100% of target?**
A: Hitting 90%+ overall is excellent! 100% is very difficult.

**Q: My retention is dropping. Help!**
A: Increase Renew budget! Also check Use (engaged customers stay).

**Q: What if I make a mistake?**
A: You can reset the simulation anytime. Learn and try again!

## Time Commitment

- **First run:** 45-60 minutes (learning + 8 quarters)
- **Subsequent runs:** 20-30 minutes
- **Analysis/Report:** 1-2 hours

## Deliverables (Check Your Assignment)

Typically you'll need to submit:

1. **Screenshot** of final results
2. **Strategy document** explaining your choices
3. **Charts** showing trends
4. **Reflection** on what you learned

## Pro Tips from Top Students

💡 **"Consistency in 2021 worked better than constant tweaking"**

💡 **"Heavy fixed investment in Q1-Q2 2022 paid off huge in Q3-Q4"**

💡 **"Retention improvement saved me $70M+ in churn"**

💡 **"Don't sleep on the Use phase - engaged customers don't leave"**

💡 **"The winning strategy isn't obvious - expect to iterate"**

## Need Help?

1. **Check the tips in the app** (💡 Strategy Tips section)
2. **Review your metrics** (are they trending up?)
3. **Ask yourself:** "What's limiting my growth?"
4. **Ask instructor** if really stuck

## Ready to Begin?

1. Launch the app: `streamlit run app.py`
2. Read the introduction
3. Plan your Q1 2021 allocation
4. Click "Run Quarter"
5. Analyze results
6. Adjust for Q2
7. Repeat!

**Remember:** This is about learning, not just hitting the target. The insights you gain about marketing, retention, and strategic planning are more valuable than any score.

Good luck! 🚀

---

**Hint:** If you want to see a winning strategy, check `examples/winning_strategy.json` - but try on your own first!
