"""
Eduvanta Academy Learning & Student Success Analytics

Synthetic K-8 educational dataset generator.

IMPORTANT:
This is synthetic educational data created for portfolio analysis.
It does not represent real students or real educational records.

The generator creates six related tables:
1. learners
2. courses
3. learning_activity
4. assessments
5. progress
6. parent_support
"""

from pathlib import Path
import random
from datetime import date, timedelta

import numpy as np
import pandas as pd


# =========================================================
# 1. REPRODUCIBILITY
# =========================================================

SEED = 42

random.seed(SEED)
np.random.seed(SEED)


# =========================================================
# 2. PROJECT PATHS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# 3. PROJECT PARAMETERS
# =========================================================

NUM_LEARNERS = 100

START_DATE = date(2025, 9, 1)
END_DATE = date(2026, 8, 31)

MONTH_STARTS = pd.date_range(
    START_DATE,
    END_DATE,
    freq="MS",
)


# =========================================================
# 4. COURSES
# =========================================================

courses = [
    {
        "course_id": "MATH01",
        "course_name": "Number Sense & Operations",
        "subject": "Mathematics",
        "grade_level": "K-2",
        "topic": "Numbers and Operations",
        "lesson_count": 12,
    },
    {
        "course_id": "MATH02",
        "course_name": "Fractions & Decimals",
        "subject": "Mathematics",
        "grade_level": "3-5",
        "topic": "Fractions and Decimals",
        "lesson_count": 14,
    },
    {
        "course_id": "MATH03",
        "course_name": "Geometry & Measurement",
        "subject": "Mathematics",
        "grade_level": "3-5",
        "topic": "Geometry and Measurement",
        "lesson_count": 12,
    },
    {
        "course_id": "MATH04",
        "course_name": "Pre-Algebra Foundations",
        "subject": "Mathematics",
        "grade_level": "6-8",
        "topic": "Algebraic Thinking",
        "lesson_count": 16,
    },
    {
        "course_id": "ELA01",
        "course_name": "Early Reading Foundations",
        "subject": "English / Language Arts",
        "grade_level": "K-2",
        "topic": "Reading Foundations",
        "lesson_count": 12,
    },
    {
        "course_id": "ELA02",
        "course_name": "Reading Comprehension",
        "subject": "English / Language Arts",
        "grade_level": "3-5",
        "topic": "Reading Comprehension",
        "lesson_count": 14,
    },
    {
        "course_id": "ELA03",
        "course_name": "Grammar & Vocabulary",
        "subject": "English / Language Arts",
        "grade_level": "3-5",
        "topic": "Grammar and Vocabulary",
        "lesson_count": 12,
    },
    {
        "course_id": "ELA04",
        "course_name": "Writing & Communication",
        "subject": "English / Language Arts",
        "grade_level": "6-8",
        "topic": "Writing and Communication",
        "lesson_count": 16,
    },
    {
        "course_id": "SCI01",
        "course_name": "Living Things & Life Science",
        "subject": "Science",
        "grade_level": "K-2",
        "topic": "Life Science",
        "lesson_count": 12,
    },
    {
        "course_id": "SCI02",
        "course_name": "Earth & Environmental Science",
        "subject": "Science",
        "grade_level": "3-5",
        "topic": "Earth and Environment",
        "lesson_count": 14,
    },
    {
        "course_id": "SCI03",
        "course_name": "Physical Science",
        "subject": "Science",
        "grade_level": "6-8",
        "topic": "Physical Science",
        "lesson_count": 15,
    },
    {
        "course_id": "READ01",
        "course_name": "Reading Fluency & Vocabulary",
        "subject": "Reading",
        "grade_level": "K-8",
        "topic": "Fluency and Vocabulary",
        "lesson_count": 14,
    },
]

courses_df = pd.DataFrame(courses)


# =========================================================
# 5. HELPER FUNCTIONS
# =========================================================

def random_date(start, end):
    """Return a random date between two dates."""
    days = (end - start).days
    return start + timedelta(days=random.randint(0, days))


def grade_band(grade):
    """Convert K-8 grade into the course grade band."""
    if grade in {"K", "1", "2"}:
        return "K-2"

    if grade in {"3", "4", "5"}:
        return "3-5"

    return "6-8"


def learning_level(score):
    """Classify learning level from performance."""
    if score < 60:
        return "Beginning"

    if score < 75:
        return "Developing"

    if score < 90:
        return "Proficient"

    return "Advanced"


def progress_status(score_change):
    """Classify progress using transparent rules."""
    if score_change >= 5:
        return "Improving"

    if score_change <= -5:
        return "Needs Attention"

    return "Stable"


def choose_grade():
    """Create a K-8 learner population with varied representation."""
    grades = ["K", "1", "2", "3", "4", "5", "6", "7", "8"]

    weights = [
        0.08,
        0.10,
        0.11,
        0.12,
        0.12,
        0.12,
        0.12,
        0.11,
        0.12,
    ]

    return random.choices(
        grades,
        weights=weights,
        k=1,
    )[0]


def badge_for_progress(score_change, completion):
    """Award recognition based on measurable progress."""
    if completion >= 100 and score_change >= 10:
        return "Progress Star"

    if completion >= 100:
        return "Course Completion"

    if score_change >= 10:
        return "Growth Champion"

    return "Learning Milestone"


def recognition_tag(score_change, completion):
    """Create a recognition label."""
    if completion >= 100 and score_change >= 10:
        return "Great Improvement"

    if completion >= 100:
        return "Successful Completion"

    if score_change >= 10:
        return "Strong Progress"

    return "Learning Progress"


# =========================================================
# 6. LEARNERS
# =========================================================

learner_records = []

for number in range(1, NUM_LEARNERS + 1):

    learner_id = f"L{number:03d}"

    grade = choose_grade()

    # Baseline academic performance.
    baseline_score = float(
        np.clip(
            np.random.normal(72, 10),
            45,
            92,
        )
    )

    # Individual learning engagement tendency.
    engagement_factor = float(
        np.clip(
            np.random.normal(0.75, 0.12),
            0.40,
            0.98,
        )
    )

    # Individual learning trajectory.
    # Positive values generally improve over time.
    growth_rate = float(
        np.clip(
            np.random.normal(0.35, 0.18),
            -0.10,
            0.75,
        )
    )

    learner_records.append(
        {
            "learner_id": learner_id,
            "grade_level": grade,
            "enrollment_date": random_date(
                START_DATE,
                START_DATE + timedelta(days=45),
            ),
            "learning_level": learning_level(
                baseline_score
            ),
            "_baseline_score": baseline_score,
            "_engagement_factor": engagement_factor,
            "_growth_rate": growth_rate,
        }
    )


learners_df = pd.DataFrame(learner_records)


# =========================================================
# 7. LEARNING ACTIVITY
# =========================================================

activity_records = []

activity_counter = 1

for learner in learner_records:

    learner_id = learner["learner_id"]
    band = grade_band(learner["grade_level"])
    engagement_factor = learner["_engagement_factor"]

    available_courses = courses_df[
        courses_df["grade_level"].isin(
            [band, "K-8"]
        )
    ]

    selected_courses = available_courses.sample(
        n=min(4, len(available_courses)),
        random_state=SEED + activity_counter,
    )

    for _, course in selected_courses.iterrows():

        number_of_activities = random.randint(
            10,
            18,
        )

        for _ in range(number_of_activities):

            activity_date = random_date(
                START_DATE,
                END_DATE,
            )

            participation_rate = float(
                np.clip(
                    engagement_factor * 100
                    + np.random.normal(0, 8),
                    25,
                    100,
                )
            )

            session_minutes = int(
                np.clip(
                    15
                    + engagement_factor * 30
                    + np.random.normal(0, 8),
                    10,
                    75,
                )
            )

            activities_completed = max(
                1,
                int(
                    round(
                        engagement_factor * 5
                        + np.random.normal(0, 1)
                    )
                ),
            )

            completion_percentage = float(
                np.clip(
                    participation_rate
                    + np.random.normal(0, 12),
                    20,
                    100,
                )
            )

            activity_records.append(
                {
                    "activity_id": f"A{activity_counter:05d}",
                    "learner_id": learner_id,
                    "course_id": course["course_id"],
                    "activity_date": activity_date,
                    "lesson_id": (
                        f"{course['course_id']}_L"
                        f"{random.randint(1, course['lesson_count']):02d}"
                    ),
                    "session_minutes": session_minutes,
                    "activities_completed": activities_completed,
                    "participation_rate": round(
                        participation_rate,
                        1,
                    ),
                    "completion_percentage": round(
                        completion_percentage,
                        1,
                    ),
                }
            )

            activity_counter += 1


learning_activity_df = pd.DataFrame(
    activity_records
)


# =========================================================
# 8. ASSESSMENTS
# =========================================================

assessment_records = []

assessment_counter = 1

for learner in learner_records:

    learner_id = learner["learner_id"]
    band = grade_band(learner["grade_level"])

    baseline = learner["_baseline_score"]
    engagement = learner["_engagement_factor"]
    growth_rate = learner["_growth_rate"]

    learner_courses = courses_df[
        courses_df["grade_level"].isin(
            [band, "K-8"]
        )
    ]

    selected_courses = learner_courses.sample(
        n=min(3, len(learner_courses)),
        random_state=SEED + assessment_counter,
    )

    for _, course in selected_courses.iterrows():

        assessment_dates = sorted(
            random_date(
                START_DATE,
                END_DATE,
            )
            for _ in range(
                random.randint(6, 9)
            )
        )

        for assessment_number, assessment_date in enumerate(
            assessment_dates
        ):

            # Months elapsed since the beginning.
            months_elapsed = (
                (assessment_date.year - START_DATE.year)
                * 12
                + assessment_date.month
                - START_DATE.month
            )

            # Engagement contributes modestly to the trajectory.
            engagement_effect = (
                engagement - 0.70
            ) * 18

            # Gradual learning improvement.
            learning_effect = (
                growth_rate
                * months_elapsed
            )

            # Small natural assessment variation.
            noise = np.random.normal(0, 3.5)

            score = (
                baseline
                + learning_effect
                + engagement_effect
                + noise
            )

            score = float(
                np.clip(
                    score,
                    35,
                    100,
                )
            )

            questions_attempted = random.randint(
                10,
                20,
            )

            questions_correct = int(
                round(
                    questions_attempted
                    * score
                    / 100
                )
            )

            questions_correct = max(
                0,
                min(
                    questions_attempted,
                    questions_correct,
                ),
            )

            score_percentage = (
                questions_correct
                / questions_attempted
            ) * 100

            # Retries are more likely when performance is lower.
            retry_probability = (
                0.10
                if score_percentage >= 80
                else 0.30
                if score_percentage >= 65
                else 0.55
            )

            retry_count = (
                1
                if random.random()
                < retry_probability
                else 0
            )

            if retry_count == 1 and score_percentage < 55:
                retry_count = 2

            assessment_type = random.choice(
                [
                    "Quiz",
                    "Practice",
                    "Test",
                ]
            )

            assessment_records.append(
                {
                    "assessment_id": (
                        f"AS{assessment_counter:05d}"
                    ),
                    "learner_id": learner_id,
                    "course_id": course["course_id"],
                    "assessment_date": assessment_date,
                    "assessment_type": assessment_type,
                    "attempt_number": retry_count + 1,
                    "questions_attempted": questions_attempted,
                    "questions_correct": questions_correct,
                    "score_percentage": round(
                        score_percentage,
                        1,
                    ),
                    "retry_count": retry_count,
                }
            )

            assessment_counter += 1


assessments_df = pd.DataFrame(
    assessment_records
)


# =========================================================
# 9. PROGRESS
# =========================================================

progress_records = []

progress_counter = 1

for (
    learner_id,
    course_id,
), group in assessments_df.groupby(
    ["learner_id", "course_id"]
):

    group = group.sort_values(
        "assessment_date"
    ).reset_index(drop=True)

    baseline_score = float(
        group.iloc[0]["score_percentage"]
    )

    # Select approximately four checkpoints.
    checkpoint_positions = np.linspace(
        0,
        len(group) - 1,
        min(4, len(group)),
        dtype=int,
    )

    checkpoint_positions = sorted(
        set(checkpoint_positions)
    )

    for position in checkpoint_positions:

        checkpoint = group.iloc[position]

        current_score = float(
            checkpoint["score_percentage"]
        )

        score_change = (
            current_score
            - baseline_score
        )

        # Course completion increases through the year.
        progress_ratio = (
            (
                checkpoint["assessment_date"]
                - START_DATE
            ).days
            / (
                END_DATE
                - START_DATE
            ).days
        )

        completion_percentage = float(
            np.clip(
                25
                + progress_ratio * 75
                + np.random.normal(0, 4),
                20,
                100,
            )
        )

        # Final checkpoint represents completed course progress.
        if position == checkpoint_positions[-1]:
            completion_percentage = 100.0

        status = progress_status(
            score_change
        )

        badge = badge_for_progress(
            score_change,
            completion_percentage,
        )

        recognition = recognition_tag(
            score_change,
            completion_percentage,
        )

        progress_records.append(
            {
                "progress_id": (
                    f"P{progress_counter:05d}"
                ),
                "learner_id": learner_id,
                "course_id": course_id,
                "progress_date": checkpoint[
                    "assessment_date"
                ],
                "starting_score": round(
                    baseline_score,
                    1,
                ),
                "current_score": round(
                    current_score,
                    1,
                ),
                "score_change": round(
                    score_change,
                    1,
                ),
                "completion_percentage": round(
                    completion_percentage,
                    1,
                ),
                "progress_status": status,
                "badge_earned": badge,
                "recognition_tag": recognition,
            }
        )

        progress_counter += 1


progress_df = pd.DataFrame(
    progress_records
)


# =========================================================
# 10. PARENT / GUARDIAN SUPPORT
# =========================================================

support_records = []

support_counter = 1

for (
    learner_id,
    course_id,
), group in assessments_df.groupby(
    ["learner_id", "course_id"]
):

    group = group.sort_values(
        "assessment_date"
    ).reset_index(drop=True)

    average_score = (
        group["score_percentage"].mean()
    )

    average_retry = (
        group["retry_count"].mean()
    )

    recent_score = float(
        group.iloc[-1]["score_percentage"]
    )

    earlier_score = float(
        group.iloc[0]["score_percentage"]
    )

    overall_change = (
        recent_score
        - earlier_score
    )

    if average_score < 60:

        observed_pattern = (
            "Repeated low assessment performance"
        )

        support_area = "Topic practice"

        suggested_support = (
            "Review the relevant topic with "
            "short, regular practice sessions."
        )

    elif average_retry >= 1.5:

        observed_pattern = (
            "Frequent assessment retries"
        )

        support_area = "Practice and review"

        suggested_support = (
            "Review missed questions and "
            "practice the topic before the "
            "next assessment."
        )

    elif overall_change <= -5:

        observed_pattern = (
            "Declining performance over time"
        )

        support_area = "Learning routine"

        suggested_support = (
            "Encourage a consistent learning "
            "routine and review challenging topics."
        )

    elif average_score < 75:

        observed_pattern = (
            "Developing assessment performance"
        )

        support_area = "Skill reinforcement"

        suggested_support = (
            "Provide additional practice and "
            "encourage the learner to explain "
            "the topic in their own words."
        )

    else:
        continue

    # Record support before the final assessment
    # so that a later assessment can measure outcome.
    support_position = random.randint(
        0,
        len(group) - 2
    )

    support_observation = group.iloc[
        support_position
    ]

    support_date = support_observation[
        "assessment_date"
    ]

    support_score = float(
        support_observation[
            "score_percentage"
        ]
    )

    future_assessments = group.iloc[
        support_position + 1:
    ]

    follow_up = future_assessments.iloc[0]

    follow_up_score = float(
        follow_up["score_percentage"]
    )

    if follow_up_score >= support_score + 5:

        outcome = "Improved"

    elif follow_up_score <= support_score - 5:

        outcome = "Needs Review"

    else:

        outcome = "Stable"

    follow_up_date = (
        follow_up["assessment_date"]
    )

    support_records.append(
        {
            "support_id": (
                f"S{support_counter:05d}"
            ),
            "learner_id": learner_id,
            "course_id": course_id,
            "support_date": support_date,
            "observed_pattern": observed_pattern,
            "support_area": support_area,
            "suggested_home_support": suggested_support,
            "follow_up_date": follow_up_date,
            "follow_up_score": round(
                follow_up_score,
                1,
            ),
            "support_outcome": outcome,
        }
    )

    support_counter += 1


parent_support_df = pd.DataFrame(
    support_records
)


# =========================================================
# 11. DATA TYPES
# =========================================================

learners_df["enrollment_date"] = pd.to_datetime(
    learners_df["enrollment_date"]
)

learning_activity_df["activity_date"] = pd.to_datetime(
    learning_activity_df["activity_date"]
)

assessments_df["assessment_date"] = pd.to_datetime(
    assessments_df["assessment_date"]
)

progress_df["progress_date"] = pd.to_datetime(
    progress_df["progress_date"]
)

parent_support_df["support_date"] = pd.to_datetime(
    parent_support_df["support_date"]
)

parent_support_df["follow_up_date"] = pd.to_datetime(
    parent_support_df["follow_up_date"]
)


# =========================================================
# 12. REMOVE INTERNAL GENERATION FIELDS
# =========================================================

learners_df = learners_df[
    [
        "learner_id",
        "grade_level",
        "enrollment_date",
        "learning_level",
    ]
]


# =========================================================
# 13. SAVE RAW TABLES
# =========================================================

tables = {
    "learners": learners_df,
    "courses": courses_df,
    "learning_activity": learning_activity_df,
    "assessments": assessments_df,
    "progress": progress_df,
    "parent_support": parent_support_df,
}


for table_name, dataframe in tables.items():

    output_path = (
        RAW_DATA_DIR
        / f"{table_name}.csv"
    )

    dataframe.to_csv(
        output_path,
        index=False,
    )


# =========================================================
# 14. GENERATION SUMMARY
# =========================================================

print(
    "Eduvanta Academy synthetic dataset "
    "generated successfully."
)

print()

print(
    "Dataset type: Synthetic educational data"
)

print(
    f"Random seed: {SEED}"
)

print(
    f"Learning period: "
    f"{START_DATE} to {END_DATE}"
)

print(
    f"Learners: {len(learners_df):,}"
)

print(
    f"Courses: {len(courses_df):,}"
)

print(
    f"Learning activities: "
    f"{len(learning_activity_df):,}"
)

print(
    f"Assessments: "
    f"{len(assessments_df):,}"
)

print(
    f"Progress records: "
    f"{len(progress_df):,}"
)

print(
    f"Parent/guardian support records: "
    f"{len(parent_support_df):,}"
)

print()

print(
    f"Files saved to: "
    f"{RAW_DATA_DIR}"
)