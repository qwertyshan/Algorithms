# Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
# To do this, you will need to know when any team is having a meeting.
# In HiCal, a meeting is stored as tuples of integers (start_time, end_time).
# These integers represent the number of 30-minute blocks past 9:00am.

# Write a function condense_meeting_times() that takes a list of meeting time ranges and returns a list of condensed ranges.

test_input = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def condense_meeting_times(input):
    list = sorted(input)

    merged = []

    prev_start, prev_end = list[0]

    # compare mtg1 every other meeting in list[]
    for (cur_start, cur_end) in list[1:]:
        if cur_start <= prev_end:
            prev_end = max(cur_end, prev_end)
        else:
            merged.append((prev_start, prev_end))
            prev_start, prev_end = cur_start, cur_end

    merged.append((prev_start, prev_end))

    return merged


print condense_meeting_times(test_input)