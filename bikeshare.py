import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#######################################################################################################################
def get_filters():
 
    cities  = ['chicago','new york city','washington']
    months  = [-1,1,2,3,4,5,6]
    days    = [-1,0,1,2,3,4,5,6]




    print('\n Hello! Lets explore some US bikeshare data!')
    print('\n would you like to see data for Chicago, New York, or Washington?')
     
     
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input()
    city = city.lower()
    while city not in cities:
              print('enetr a valid city name please!\n')
              city = input()



    # TO DO: get user input for month (all, january, february, ... , june)
    print('\n eneter the month please as an integer : 1 = January - 6 = June',
          ' , or enter -1 for skipping the month')
    month = int(input())
    #month = month.lower() 
    while month not in months:
         print('enetr a valid month integer please!\n')
         month = int(input())



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\n eneter the day please:  (0 Sunday) - (6 saturday)',
          ' , or enter -1 for skipping the day')
    day = int(input())
    while day not in days:
         print('enetr a valid day integer  please!\n')
         day = int(input())



    print('-'*40)
    return city, month, day
#####################################################################################################################
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
  
    
    

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
   
    #df = df[df['Start Time'].dt.month==month]
    #df = df[df['Start Time'].dt.dayofweek==day]

    
    
    
    

    # filter by month if applicable
    if month != -1:
       
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != -1:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

################################################################################################################
    
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df['month'].mode()[0]
    print("the most popular month is " , com_month)

    # TO DO: display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print("the most popular day is " , com_day)

    # TO DO: display the most common start hour
    
    com_hour = df['hour'].mode()[0]
    print("the most popular hour is " , com_hour)
    
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
######################################################################################################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    station_Start = df['Start Station'].mode()[0]
    print("the most popular Srat station is " , station_Start)
   

    # TO DO: display most commonly used end station
    station_End = df['End Station'].mode()[0]
    print("the most popular End station is " , station_End)

    # TO DO: display most frequent combination of start station and end station trip

    lis = ['Start Station','End Station']
    
    combo = df[lis].mode()
    print("the most popular Combo of Start Statio and End station is " , combo['Start Station'][0] ,' and ' , combo['End Station'][0] )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#######################################################################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()



    # TO DO: display total travel time
    trip_dur = df['Trip Duration'].sum()
    print(' the total travel time is  ' , trip_dur)



    # TO DO: display mean travel time
    trip_dur = df['Trip Duration'].mean()
    print(' the average travel time is  ' , trip_dur)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#######################################################################################################################

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('\n the counts of user types is \n' , user_count)



    if city != 'washington':
    # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('\n the counts of Gender is \n ' , gender_count)

    # TO DO: Display earliest, most recent, and most commowashingtonn year of birth
   
        dob_earliest =  df['Birth Year'].max()
        dob_recent =  df['Birth Year'].min()
        com_dob = df['Birth Year'].mode()[0]
        print('\n the earliest year is ' , dob_earliest ,
              ' the most recent year is  ' , dob_recent , ' the most common yeaar of birth is  ' , com_dob )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#######################################################################################################################

def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)
       
       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df,city)
       
       
       sample = input('\nWould you like a smaple? Enter yes or no.\n')
       if sample.lower() == 'yes':
         print(df.head())
         break 
       
       restart = input('\nWould you like to restart? Enter yes or no.\n')
       if restart.lower() != 'yes':
         break
       
   
if __name__ == "__main__":
    main()
