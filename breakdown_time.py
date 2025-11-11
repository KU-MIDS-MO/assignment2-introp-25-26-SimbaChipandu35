def breakdown_time(seconds):
  
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    result = {}
    for time in [3600, 60, 1]:
        count = seconds // time
        if count > 0:
            result[time] = count
            seconds = seconds % time
    return result
