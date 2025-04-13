from stops.models import Stop, Agency


def fc27():
    fact = """
    During those (2023) stops, Black drivers were more likely to get traffic tickets, while white drivers were more likely to drive away with warnings. About 1 in 3 Black drivers received a ticket rather than a verbal or written warning in comparison to 1 in 5 white drivers, according to an analysis of the most recent five years.    
    """
    
    y23 = Stop.objects.all()
    y23b, y23w = y23.filter(driver_race='Black'), y23.filter(driver_race='White')
    y23b_tix, y23w_tix = y23b.filter(outcome='Citation'), y23w.filter(outcome='Citation')
    print('FC 27')
    print(fact)
    print('####')

    print('2023 stops')
    print('Black driver ticket rate:',y23b_tix.count()/float(y23b.count()))
    print('White driver ticket rate:',y23w_tix.count()/float(y23w.count()))



