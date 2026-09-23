"""
Day 2 tools:
1. get_course_fee()
2. calculator()
"""

COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}


def get_course_fee(course_code):
    """
    Return the fee for a course.
    """
    course_code = course_code.upper()

    if course_code not in COURSE_FEES:
        raise ValueError(f"Unknown course code: {course_code}")

    return COURSE_FEES[course_code]


def calculator(expression):
    """
    Calculate a mathematical expression.
    """
    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )
        return result
    except Exception as e:
        return f"Calculation error: {e}"