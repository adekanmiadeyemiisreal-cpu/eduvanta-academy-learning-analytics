# Eduvanta Academy Learning Analytics

## Project Overview

Eduvanta Academy Learning Analytics is an end-to-end education data analytics project designed to transform learner activity, assessment, progress, and support data into actionable insights.

The project demonstrates how Python and Power BI can be used to monitor learner performance, engagement, completion, and progress.

## Business Problem

Educational platforms generate large amounts of learner data, but raw data alone does not clearly show:

- How learners are performing
- Which subjects have stronger or weaker performance
- How learner participation relates to completion
- Which learners are improving
- Which learners may require additional attention
- Where educators can focus interventions

This project addresses these questions through data exploration, analysis, and interactive visualization.

## Objectives

- Analyze learner assessment performance
- Measure learner participation and completion
- Evaluate progress and score changes
- Compare performance across subjects/courses
- Identify learners and patterns requiring attention
- Build an interactive Power BI dashboard
- Generate actionable recommendations from the data

## Dataset

The project uses education-related datasets covering:

- Learners
- Courses
- Learning activities
- Assessments
- Progress
- Parent/support records

The dataset contains records for 100 learners.

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Power BI
- DAX
- GitHub

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Learners | 100 |
| Average Assessment Score | 75.26% |
| Average Score Change | 1.69 |
| Average Completion | 62.35% |
| Average Participation | 72.76% |

## Key Analysis

### Subject Performance

Mathematics recorded the highest average assessment score at 75.56%, while English / Language Arts recorded the lowest at 74.97%.

Overall performance was relatively consistent across the four subjects.

### Learner Engagement and Completion

Learners with the highest participation rates showed substantially higher completion rates than learners with the lowest participation rates.

The correlation between average participation and average completion was **0.988**, indicating a very strong positive relationship in this dataset.

Correlation should not be interpreted as proof of causation.

### Progress Status

Improving learners recorded an average score change of **+8.50 points** and an average completion rate of **75.92%**.

Learners classified as Needs Attention recorded an average score change of **-7.70 points**, indicating a decline in assessment performance.

### Learner Performance

The highest-performing learners had average assessment scores ranging from approximately **91.19% to 96.27%**.

The lowest-performing learners ranged from approximately **55.15% to 62.54%**, showing a substantial performance gap within the learner population.

## Power BI Dashboard

The Power BI dashboard contains:

1. Average Score Percentage by Course ID
2. Count of Learners by Progress Status
3. Average Completion Percentage by Course ID
4. Average Participation Rate by Course ID
5. Average Score Change by Course ID

The dashboard also includes five KPI cards summarizing overall learner performance.

## Recommendations

Based on the analysis:

- Monitor learners with declining score changes.
- Investigate low-participation patterns early.
- Encourage activities that increase learner engagement.
- Provide targeted academic support for learners requiring attention.
- Monitor completion rates alongside participation.
- Use course-level performance comparisons to identify areas for instructional improvement.

## Project Structure

```text
Eduvanta-Academy-Learning-Analytics/
│
├── .venv/
├── Notebooks/
│   └── 01 data exploration.ipynb
├── Src/
│   ├── Generate data.py
│   └── Generate data backup.py
├── Visualizations/
├── .gitignore
└── README.md
## Project Outcome

This project demonstrates an end-to-end analytics workflow:

**Data Generation → Data Exploration → Data Analysis → KPI Development → Power BI Visualization → Business Insights → Recommendations**

## Future Development

Potential future extensions include:

- Automated reporting
- Predictive learner-risk analysis
- AI-generated learner insights
- Real-time education analytics
- An education analytics SaaS platform

## Author

**Adekanmi Adeyemi Isreal**

Data Analyst | Business & Economic Researcher | BI & Analytics