from stops.models import Agency, AgencyData
import csv

# lookups
police_demographics = {
    'BRADLEY UNIVERSITY POLICE': 'Bradley University',
    'CHICAGO STATE UNIVERSITY POLICE': 'Chicago State University',
    'COLLEGE OF DUPAGE POLICE': 'College of DuPage',
    'COLLEGE OF LAKE COUNTY POLICE': 'College of Lake County',
    'EASTERN ILLINOIS UNIVERSITY POLICE': 'Eastern Illinois University',
    'ELGIN COMMUNITY COLLEGE POLICE': 'Elgin Community College',
    'HARPER COLLEGE POLICE': 'Harper College',
    'ILLINOIS STATE UNIVERSITY POLICE': 'Illinois State University',
    'JOHN A LOGAN COLLEGE POLICE': 'John A. Logan College',
    'JOLIET JUNIOR COLLEGE POLICE': 'Joliet Junior College',
    'LAKE LAND COLLEGE POLICE': 'Lake Land College',
    'LINCOLN LAND COMMUNITY COLLEGE POLICE': 'Lincoln Land Community College',
    'MORAINE VALLEY COMMUNITY COLLEGE POLICE': 'Moraine Valley Community College',
    'NORTHEASTERN ILLINOIS UNIVERSITY POLICE': 'Northeastern Illinois University',
    'NORTHERN ILLINOIS UNIVERSITY POLICE': 'Northern Illinois University',
    'NORTHWESTERN UNIVERSITY POLICE': 'Northwestern University',
    'OAKTON COMMUNITY COLLEGE POLICE': 'Oakton Community College',
    'PARKLAND COLLEGE POLICE': 'Parkland College',
    'ROCK VALLEY COLLEGE POLICE': 'Rock Valley College',
    'SOUTH SUBURBAN COLLEGE POLICE': 'South Suburban Coll. of Cook Co.',
    'SOUTHERN ILLINOIS UNIVERSITY CARBONDALE POLICE': 'Southern Illinois University Carbondale',
    'SOUTHERN ILLINOIS UNIVERSITY EDWARDSVILLE POLICE': 'Southern Illinois University Edwardsville',
    'SOUTHWESTERN ILLINOIS COLLEGE POLICE': 'Southwestern Illinois College',
    'TRITON COLLEGE POLICE': 'Triton College',
    'UNIVERSITY OF CHICAGO POLICE': 'University of Chicago',
    'UNIVERSITY OF ILLINOIS CHICAGO POLICE': 'University of Illinois Chicago',
    'UNIVERSITY OF ILLINOIS SPRINGFIELD POLICE': 'University of Illinois Springfield',
    'UNIVERSITY OF ILLINOIS URBANA POLICE': 'University of Illinois Urbana/Champaign',
    'WAUBONSEE COMMUNITY COLLEGE POLICE': 'Waubonsee Community College',
    'WESTERN ILLINOIS UNIVERSITY POLICE': 'Western Illinois University',
    'BENEDICTINE UNIVERSITY POLICE': 'Benedictine University',
    'GOVERNORS STATE UNIVERSITY POLICE': 'Governors State University',
    'JOHNWOOD COMMUNITY COLLEGE CAMPUS POLICE': 'John Wood Community College',
    'MORTON COLLEGE POLICE': 'Morton College',
    'LEWIS UNIVERSITY POLICE': 'Lewis University',
    'MCHENRY COUNTY COLLEGE POLICE': 'McHenry County College',
    'REND LAKE COLLEGE POLICE': 'Rend Lake College',
    'MILLIKIN UNIVERSITY POLICE': 'Millikin University',
    'SOUTHERN ILLINOIS UNIVERSITY SCHOOL OF MEDICINE POLICE': 'Southern Illinois University School of Medicine',
    'ILLINOIS CENTRAL COLLEGE POLICE': 'Illinois Central College',
    'LOYOLA UNIVERSITY POLICE': 'Loyola University of Chicago',
    'EUREKA COLLEGE PD': 'Eureka College',
    'RICHLAND COMMUNITY COLLEGE PD': 'Richland Community College',
    'KASKASKIA COLLEGE PD': 'Kaskaskia College'
}

# derive agency query from above
agencies = Agency.objects.filter(name__in=police_demographics.keys())

# college demographic data
demos = [x for x in csv.DictReader(open('school_demos.csv'))]
# the fields we'll use
demo_keys = ['Afr-Amer, Black','Amer Indian, AK Native','Asian','Hispanic','Native Hawaii, Other Pacific','White','2+ races','Intl. Stud.','Unknown','Total']


# populate agencydata
for agency in agencies:
    # translate police agency name to name found in demographics data
    college_name = police_demographics[agency.name]
    # get demos for that college
    try: 
        college_demos = [x for x in demos if x['Institution'] == college_name][0]
    except IndexError as e:
        print("couldn't find demos for",agency.name)
        continue
    # loop through demo fields
    for field in demo_keys:
        # create agencydata record
        ad = AgencyData.objects.create(
                agency = agency,
                agency_name = college_name,
                metric = field,
                value = college_demos[field]
                )
        ad.save()
