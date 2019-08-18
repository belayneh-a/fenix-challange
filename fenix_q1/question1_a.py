import sys

'''
 Fenix Full Stack Software Challenge:
 For Question 1 (a,b)
'''

# Implementation of the solution is not only for the case of 4 arguments rather it works for N number of arguments
# In order to comply with the challenge default case of execution 3 should be chosen as No loans number(3 args + K)
# the beginning of execution


class LoanMgt:
    loans = {}
    def __init__(self, r1, d1, r2, d2, r3, d3, k):
        r1 = sys.argv[1]
        d1 = sys.argv[2]
        r2 = sys.argv[3]
        d2 = sys.argv[4]
        r3 = sys.argv[5]
        d3 = sys.argv[6]
        k = sys.argv[7]
        self.loans = {d1: r1, d2: r2, d3: r3}

        # validating inputs
        if isinstance(k, int) and k > 0:
            self.amount = k
        else:
            # exit(print('There is no paid amount'))
            sys.exit(print('There is no paid amount'), 3)
        #
        # escaping error for delete dictionary during iteration in case of 0 days
        try:
            for nth_days, nth_loan in self.loans.items():
                if isinstance(nth_loan, int) and nth_loan > 0:
                    pass
                else:
                    sys.exit(print('loan could not be less than 0'), 3)
                if int(nth_days) > 0:
                    pass
                else:
                    del self.loans[nth_days]
        except:
            pass

    def get_daysof_power(self):
        daysof_power = 0
        cumilative_rate = self.__get_cum_rate_per_day()
        for days, daily_rate in cumilative_rate.items():
            i_day = int(days)
            if self.amount >= daily_rate:
                while i_day > 0 or days == -1:
                    if self.amount >= daily_rate:
                        self.amount -= daily_rate
                        i_day -= 1
                        daysof_power += 1
                    else:
                        break
            else:
                break
        return daysof_power

    def __get_cum_rate_per_day(self):
        self.loans = dict(sorted(self.loans.items()))
        cumilative_pays = {}
        ld_length = len(self.loans)
        c_days = -1
        c_loan = -1
        for days, loan in self.loans.items():
            if c_days == -1:
                c_days = days
                c_loan = loan
            else:
                if abs(c_days - days) == 0:
                    c_loan += loan
                    cumilative_pays.update({c_days: c_loan})
                    continue
                else:
                    cumilative_pays.update({abs(c_days - days): c_loan})
                    c_loan += loan
                c_days = days
                ld_length -= 1
            if ld_length == 1:
                cumilative_pays.update({-1: c_loan})
        return cumilative_pays


if __name__ == '__main__':
	# To be updated for test and running
     x_loan = LoanMgt()
     x_loan.get_daysof_power()