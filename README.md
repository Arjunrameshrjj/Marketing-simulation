# 🎓 DDOM Marketing Simulation

An interactive educational platform for students to learn marketing budget allocation using the DDOM framework (Discover, Try, Buy, Use, Renew).

## 📋 Overview

This simulation is based on real marketing principles and challenges students to:
- Allocate $250M (2021) or $300M (2022) quarterly budgets
- Maximize Net-New Annual Recurring Revenue (ARR)
- Balance short-term results vs. long-term investment
- Achieve 97%+ of $4.5B total target across 8 quarters

## 🚀 Quick Start

### Quick Start

1. **Clone or download this repository**
2. **Open `index.html`** in any modern web browser.

No installation or server is required. This is a pure static application.

## 🌐 Deployment

Since this is a static site, you can host it for free on:
- **GitHub Pages**: Push this repo and enable Pages in settings.
- **Render**: Connect your repo and choose **Static Site**.
- **Netlify/Vercel**: Drag and drop the folder or connect your repo.

## 🎯 How to Use

### The Challenge

You have **8 quarters** (Q1-Q4 2021, Q1-Q4 2022) to manage:

**2021:**
- Budget: $250M per quarter
- Target: $500M Net-New ARR per quarter
- Total Target: $2B

**2022:**
- Budget: $300M per quarter
- Target: $625M Net-New ARR per quarter
- Total Target: $2.5B

### The 5 Budget Phases (DDOM)

1. **🌐 Discover** (Drive Website Traffic)
   - Variable: Awareness Marketing
   - Fixed: Landing Page Optimization

2. **🔍 Try** (Convert Visitors to Trials)
   - Variable: Consideration Marketing
   - Fixed: Recommendation Engine

3. **💰 Buy** (Convert Trials to Customers)
   - Variable: Performance Marketing
   - Fixed: E-Commerce Optimization

4. **🎮 Use** (Engage Customers)
   - Variable: Engagement Marketing
   - Fixed: Product Engagement

5. **🔄 Renew** (Retain Customers)
   - Variable: Save Offers
   - Fixed: Payment Processing

### Understanding Variable vs. Fixed

- **Variable Spend**: Immediate impact this quarter
- **Fixed Spend**: Improves conversion rates starting NEXT quarter (compounds over time)

### Key Formula

```
Net-New ARR = Gross New ARR - Cancel ARR
```

- **Gross ARR**: Revenue from new customer orders
- **Cancel ARR**: Revenue lost from churned customers
- Higher retention = Lower Cancel ARR

## 💡 Strategy Guide

### Recommended Approach

**2021 Strategy (Foundation Building):**
- Q1-Q4: Use consistent allocation
- Focus: 40% on Buy phase
- Fixed: Keep low (5-10%) to maximize immediate results
- Goal: Build customer base and momentum

**2022 Strategy (Leverage & Optimize):**
- Q1-Q3: Heavy fixed investment (15-20%)
- Q4: Shift to higher variable spend
- Focus: Balanced across all phases
- Goal: Leverage 2021 foundation for breakthrough

### Common Patterns

1. **Q1 Underperformance**: Normal! You'll achieve ~80-85% of target
2. **Q2 Breakthrough**: Benefits from Q1 fixed investments (+15-25% jump)
3. **Q3-Q4 Plateau**: Optimization phase, steady results

### Pro Tips

✅ **Do:**
- Maintain balance (no single phase >45%)
- Invest in fixed early (Q1-Q2)
- Keep Renew spend at 5-10%
- Be patient - compounding takes time

❌ **Don't:**
- Over-index on one phase
- Cut Renew below 5% (churn will spike)
- Change strategy every quarter
- Panic if Q1 is low

## 📊 Exit Criteria (Q4 2022)

To successfully complete the simulation:

- ✅ Website Visitors > 135M
- ✅ Free Trialists > 12.7M
- ✅ Orders > 1.5M
- ✅ Retention Rate > 70%
- ✅ Total ARR ≥ 90% of target ($4.05B+)

## 🎯 Winning Strategy Example

Based on successful student attempts:

### 2021 (All Quarters):
```
Discover: $46M variable + $6M fixed = $52M (20.8%)
Try: $34M variable + $6M fixed = $40M (16%)
Buy: $94M variable + $6M fixed = $100M (40%)
Use: $36M variable + $6M fixed = $42M (16.8%)
Renew: $12M variable + $4M fixed = $16M (6.4%)
Total: $250M
```
**Expected:** ~$520M per quarter, 98% of 2021 target

### 2022 Q1-Q3:
```
Discover: $56M variable + $12M fixed = $68M (22.7%)
Try: $46M variable + $12M fixed = $58M (19.3%)
Buy: $78M variable + $18M fixed = $96M (32%)
Use: $38M variable + $12M fixed = $50M (16.7%)
Renew: $16M variable + $12M fixed = $28M (9.3%)
Total: $300M
```
**Expected:** $536M (Q1) → $616M (Q2-Q3)

### 2022 Q4 (Final Push):
```
Discover: $58M variable + $10M fixed = $68M (22.7%)
Try: $48M variable + $10M fixed = $58M (19.3%)
Buy: $82M variable + $12M fixed = $94M (31.3%)
Use: $41M variable + $10M fixed = $51M (17%)
Renew: $19M variable + $10M fixed = $29M (9.7%)
Total: $300M
```
**Expected:** $625-630M (100%+ of target!)

## 📈 What Students Learn

1. **Budget Allocation**: Balancing competing priorities
2. **Time Value**: Short-term vs. long-term investments
3. **Compound Returns**: How fixed investments build over time
4. **Customer Retention**: Why retention is a growth multiplier
5. **Strategic Planning**: 8-quarter planning horizon
6. **Data-Driven Decisions**: Using KPIs to optimize
7. **Trade-offs**: Budget constraints force choices

## 🔧 Technical Details

### Simulation Engine

The simulation uses a sophisticated model that:
- Calculates conversion rates based on spend levels
- Applies diminishing returns at high spend
- Compounds fixed investments over quarters
- Simulates market conditions (Q1 underperformance, Q2 boosts)
- Models customer churn based on retention

### Key Metrics Calculated

- **Website Visitors**: f(Awareness spend, cumulative fixed)
- **Trialists**: Visitors × Trial Conversion Rate
- **Orders**: f(Performance Marketing spend, cumulative fixed)
- **Gross ARR**: Orders × Avg Contract Value ($600)
- **Retention**: f(Save Offers, Payment Processing, MAU)
- **Cancel ARR**: -(Customer Base × Churn Rate × Avg Value)
- **Net-New ARR**: Gross ARR + Cancel ARR

## 📁 File Structure

```
marketing_simulation/
├── index.html              # Main application (React Frontend)
├── simulation_engine.js    # Core simulation logic (JavaScript)
├── README.md               # This file
└── examples/               # Example strategies
└── examples/              # Example strategies
    ├── winning_strategy.json
    └── analysis_notebook.ipynb
```

## 🎓 For Educators

### Learning Objectives

After completing this simulation, students will:
1. Understand the customer lifecycle (DDOM framework)
2. Practice budget allocation under constraints
3. Learn the importance of retention economics
4. Experience compounding returns
5. Develop strategic planning skills

### Grading Rubric Suggestion

- **90%+ of target**: A+ (Outstanding)
- **85-89% of target**: A (Excellent)
- **80-84% of target**: B+ (Very Good)
- **75-79% of target**: B (Good)
- **70-74% of target**: C+ (Satisfactory)
- **<70% of target**: C or below

### Discussion Questions

1. Why does Q1 consistently underperform?
2. What's the optimal balance between variable and fixed spend?
3. How does retention rate impact total ARR?
4. When should you reduce fixed investment?
5. What happens if you over-index on one phase?

## 🐛 Troubleshooting

**Issue**: Application won't start
- **Solution**: Ensure you are opening `index.html` in a modern browser (Chrome, Edge, Safari).

**Issue**: Budget won't validate
- **Solution**: Total must equal exactly $250M (2021) or $300M (2022)

**Issue**: Results seem unrealistic
- **Solution**: The model is calibrated to real patterns. Q1 underperformance is intentional!

## 📝 License

This educational simulation is provided for academic use. Feel free to modify and adapt for your courses.

## 🤝 Contributing

Suggestions for improvements:
- Additional scenarios (different industries)
- More detailed analytics
- Competitor simulation
- Team collaboration features

## 📧 Support

For questions or issues, please refer to the in-app help or consult the Strategy Tips section.

---

**Happy Simulating! 🚀**
