class Solution:

    def __init__(self, days):
        self.days = days
        self.ways_to_attend = self._ways_to_attend_classes()
    
    def number_of_ways_to_attend_classes(self):
        '''
        Return the number of ways to attend classes
        '''
        return len(self.ways_to_attend)

    def probability_to_miss_gradution_ceremony(self):
        '''
        Returns the result based on the format ->
        The probability that you will miss your graduation ceremony. / The number of ways to attend classes over N days.
        '''
        count_missed_your_graduation_day = self._missed_your_graduation_day()
        return "{0} / {1}".format(count_missed_your_graduation_day, self.number_of_ways_to_attend_classes())

    def _ways_to_attend_classes(self):
        arr = []
        pattern = ""
        self._util(self.days, pattern, arr)
        return arr
    
    def _util(self, days, pattern, arr):
        if days == 0:
            absent_in_class = pattern.count('AAAA') # condition -> You are not allowed to miss classes for four or more consecutive days.
            if absent_in_class==0:
                arr.append(pattern)
        else:
            self._util(days - 1, pattern + 'A', arr)
            self._util(days - 1, pattern + 'P', arr)
    
    def _missed_your_graduation_day(self):
        # Your graduation ceremony is on the last day of the academic year, which is the Nth day.
        return len(list(filter(lambda way: "A" == way[-1], self.ways_to_attend)))
    