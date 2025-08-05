def sortPeople(names, heights):
        combined = zip(heights, names)
        sorted_people = sorted(combined, reverse = True)
        return [name for height, name in sorted_people]