from stops.models import Stop, Agency

# our list of public university agencies
pub_uni_agencies = Agency.objects.filter(name__in=["EASTERN ILLINOIS UNIVERSITY POLICE", "GOVERNORS STATE UNIVERSITY POLICE","ILLINOIS STATE UNIVERSITY POLICE", "NORTHEASTERN ILLINOIS UNIVERSITY POLICE", "NORTHERN ILLINOIS UNIVERSITY POLICE", "SOUTHERN ILLINOIS UNIVERSITY CARBONDALE POLICE", "SOUTHERN ILLINOIS UNIVERSITY EDWARDSVILLE POLICE", "UNIVERSITY OF ILLINOIS CHICAGO POLICE","UNIVERSITY OF ILLINOIS SPRINGFIELD POLICE", "UNIVERSITY OF ILLINOIS URBANA POLICE", "WESTERN ILLINOIS UNIVERSITY POLICE"])

# stops just by pub unis
pub_stops = Stop.objects.filter(agency__in=pub_uni_agencies)

# just pub uni stops since 2019
y19_23 = pub_stops.filter(year__gte=2019)

# just 2023
y23 = pub_stops.filter(year=2023)

# 2023, black and white drivers
y23b, y23w = y23.filter(driver_race='Black'), y23.filter(driver_race='White')
# 2023 tickets, black and white
y23b_tix, y23w_tix = y23b.filter(outcome='Citation'), y23w.filter(outcome='Citation')



def fc25():
    #TODO 
    """NEED TO IMPORT ENROLLMENT DATA"""
    """Black drivers have been pulled over at rates that eclipsed enrollment since at least 2019, according to a new analysis of 33,388 traffic stops by officers at campus police departments at Illinois' eight public four-year colleges and their 11 campuses"""
    print('FC 25')
    print(fact)
    print('####')

    print("stops since 2019 at public unis:",y19_23.count())


def fc26():
    #TODO 
    """NEED TO IMPORT ENROLLMENT DATA"""
    """In 2023, the last full year for which data was available, the rate of Black drivers stopped was higher than the enrollment rate of Black students at all seven public colleges who reported traffic stops."""
    print('FC 26')
    print(fact)
    print('####')
    for agency in pub_uni_agencies:
        print(agency.name,'stops of Black drivers:',y23b.filter(agency=agency).count())


def fc27():
    fact = """
    During those (2023) stops, Black drivers were more likely to get traffic tickets, while white drivers were more likely to drive away with warnings. About 1 in 3 Black drivers received a ticket rather than a verbal or written warning in comparison to 1 in 5 white drivers, according to an analysis of the most recent five years.    
    """
    print('FC 27')
    print(fact)
    print('####')

    print('2023 Black driver ticket rate:',y23b_tix.count()/float(y23b.count()))
    print('2023 White driver ticket rate:',y23w_tix.count()/float(y23w.count()))


def fc28():
    fact = """Although the overall number of traffic stops has declined since the pandemic, the rate of Black drivers stopped by police has increased. Traffic stops of Black people increased from 28 percent in 2018 to 34 percent in 2023. Meanwhile, the rate of white drivers stopped by campus police decreased from 54 percent in 2018 to 45 percent in 2023."""
    print('FC 28')
    print(fact)
    print('####')

    print('year','stops','pct_blk','pct_wh')
    for year in range(2004,2024):
        year_stops = pub_stops.filter(year=year)
        bstops, wstops = year_stops.filter(driver_race='Black'), year_stops.filter(driver_race='White')
        print(year,year_stops.count(),bstops.count()/float(year_stops.count()),wstops.count()/float(year_stops.count()))


def fc47():
    fact = """Black people made up 53 percent of the 3,245 traffic stops by [NIU] campus police from 2018 through 2023, though Black students made up 17 percent of student enrollment in 2022."""
    print('FC 47')
    print(fact)
    print('####')
    
    niu = Agency.objects.get(name="NORTHERN ILLINOIS UNIVERSITY POLICE")
    niu18_23 = Stop.objects.filter(agency=niu,year__gte=2018)
    niu18_23b = niu18_23.filter(driver_race='Black')
    print('niu stops since 2018:',niu18_23.count())
    print('niu stops of black drivers since 2018:',niu18_23b.count())
    print('pct black drivers stopped by niu since 2018:',niu18_23b.count()/float(niu18_23.count()))

    
def fc52():
    #TODO: load enrollment data
    fact = """The widest disparity between traffic stops and enrollment by race was at the University of Illinois at Chicago."""
    print('FC 52')
    print(fact)
    print('####')


def fc53():
    fact = """There, Black drivers make up nearly 50 percent of traffic stops by campus police while Black students make up 8 percent of enrollment."""
    print('FC 53')
    print(fact)
    print('####')


def fc60():
    fact = """Black drivers received roughly 50 percent of tickets, though student enrollment in 2022 at those colleges was 18 and 15 percent, respectively."""
    print('FC 60')
    print(fact)
    print('####')


def fc69():
    fact = """The Investigative Project found that the racial disparities are pervasive across the state’s public universities."""
    print('FC 69')
    print(fact)
    print('####')


def fc70():
    fact = """For Illinois State University, 26 percent of the 3,916 traffic stops are of Black drivers, while only 11 percent of its enrollment are Black students. """
    print('FC 70')
    print(fact)
    print('####')


def fc79():
    fact = """Black drivers stopped by Illinois’ public campus police officers were more likely to get traffic tickets, while white drivers were more likely to get a warning, according to the analysis."""
    print('FC 79')
    print(fact)
    print('####')


def fc80():
    fact = """Among the 11 campus police departments, the widest spread between the rates of white and Black drivers getting warnings was at the University of Illinois Urbana-Champaign. There, Black drivers were nearly twice as likely to receive a ticket compared to white drivers."""
    print('FC 80')
    print(fact)
    print('####')


def fc109():
    fact = """The pandemic left many college campuses bare, which meant fewer drivers on the road and fewer people being pulled over by campus police. However, Black drivers were still overwhelmingly stopped."""
    print('FC 109')
    print(fact)
    print('####')


def fc110():
    fact = """The Investigative Project found that the rate of traffic stops decreased by 1% for Black drivers versus by 4% for white drivers during the pandemic, from 2020 to 2023."""
    print('FC 110')
    print(fact)
    print('####')


def fc121():
    fact = """The campus police department at her school had not reported any verbal warnings in the data that year."""
    print('FC 121')
    print(fact)
    print('####')


def fc122():
    fact = """Campus police there stopped 1,093 Black women, the most of any of the six public colleges reporting data from 2019 through 2023."""
    print('FC 122')
    print(fact)
    print('####')

    for agency in pub_uni_agencies:
        stops19_23 = Stop.objects.filter(agency=agency,year__gte=2019)
        stops_bw = stops19_23.filter(driver_race='Black',DriverSex='2')
        print(agency.name,stops_bw.count())


def fc123():
    fact = """Black women were nearly 40 percent of all Black people stopped at the campus during that same time period."""
    print('FC 123')
    print(fact)
    print('####')

    uiuc = Agency.objects.get(name='UNIVERSITY OF ILLINOIS URBANA POLICE')
    uiuc19_23 = Stop.objects.filter(agency=uiuc,year__gte=2018)
    uiuc_b = uiuc19_23.filter(driver_race='Black')
    uiuc_bw = uiuc_b.filter(DriverSex="2")
    print(uiuc19_23.count(),uiuc_b.count(),uiuc_bw.count())

