# Links of The Times to scrape articles
from strenum import StrEnum


class Politics(StrEnum):
    SECTION = 'Politics'

    UK_POLITICS = 'UK Politics'
    UK_POLITICS_URL = 'https://www.thetimes.co.uk/topic/uk-politics?page='

    GLOBAL_POLITICS = 'Global Politics'
    GLOBAL_POLITICS_URL = 'https://www.thetimes.co.uk/topic/global-politics?page='

    BREXIT = 'Brexit'
    BREXIT_URL = 'https://www.thetimes.co.uk/topic/brexit?page='


class Business(StrEnum):
    SECTION = 'Business & Finance'

    # Times Enterprise Network ??
    ECONOMY = 'Economy'
    ECONOMY_URL = 'https://www.thetimes.co.uk/topic/economics?page='

    MARKETS = 'Markets'
    MARKETS_URL = 'https://www.thetimes.co.uk/topic/markets?page='

    PROPERTY = 'Property'
    PROPERTY_URL = 'https://www.thetimes.co.uk/topic/real-estate?page='

    PERSONAL_FINANCE = 'Personal Finance'
    PERSONAL_FINANCE_URL = 'https://www.thetimes.co.uk/topic/personal-finance?page='

    BANKING = 'Banking'
    BANKING_URL = 'https://www.thetimes.co.uk/topic/banking?page='


class Society(StrEnum):
    SECTION = 'Society'

    HEALTH = 'Health'
    HEALTH_URL = 'https://www.thetimes.co.uk/topic/health?page='

    SCIENCE = 'Science'
    SCIENCE_URL = 'https://www.thetimes.co.uk/topic/science?page='

    TECHNOLOGY = 'Technology'
    TECHNOLOGY_URL = 'https://www.thetimes.co.uk/topic/technology?page='

    TRANSPORT = 'Transport'
    TRANSPORT_URL = 'https://www.thetimes.co.uk/topic/transport?page='

    LAW = 'Law'
    LAW_URL = 'https://www.thetimes.co.uk/topic/law?page='


class Sport(StrEnum):
    SECTION = 'Sport'

    # Football??
    CRICKET = 'Cricket'
    CRICKET_URL = 'https://www.thetimes.co.uk/topic/cricket?page='

    TENNIS = 'Tennis'
    TENNIS_URL = 'https://www.thetimes.co.uk/topic/tennis?page='

    RUGBY_UNION = 'Rugby Union'
    RUGBY_UNION_URL = 'https://www.thetimes.co.uk/topic/rugby-union?page='

    FORMULA_ONE = 'Formula One'
    FORMULA_ONE_URL = 'https://www.thetimes.co.uk/topic/formula-one?page='

    GOLF = 'Golf'
    GOLF_URL = 'https://www.thetimes.co.uk/topic/golf?page='

    RACING = 'Racing'
    RACING_URL = 'https://www.thetimes.co.uk/topic/racing?page='

    BOXING = 'Boxing'
    BOXING_URL = 'https://www.thetimes.co.uk/topic/boxing?page='

    OLYMPICS = 'Olympics'
    OLYMPICS_URL = 'https://www.thetimes.co.uk/topic/winter-olympics?page='


class ArtsAndCulture(StrEnum):
    SECTION = 'Arts & Culture'

    TV = 'TV'
    TV_URL = 'https://www.thetimes.co.uk/topic/television?page='

    FILM = 'Film'
    FILM_URL = 'https://www.thetimes.co.uk/topic/film?page='

    MUSIC = 'Music'
    MUSIC_URL = 'https://www.thetimes.co.uk/topic/music?page='

    RADIO_AND_PODCASTS = 'Radio & Podcasts'
    RADIO_AND_PODCASTS_URL = 'https://www.thetimes.co.uk/topic/radio?page='

    BOOKS = 'Books'
    BOOKS_URL = 'https://www.thetimes.co.uk/topic/books?page='

    THEATRE = 'Theatre'
    THEATRE_URL = 'https://www.thetimes.co.uk/topic/theatre?page='

    ART = 'Art'
    ART_URL = 'https://www.thetimes.co.uk/topic/art?page='


class LifeAndStyle(StrEnum):
    SECTION = 'Life & Style'

    BEAUTY = 'Beauty'
    BEAUTY_URL = 'https://www.thetimes.co.uk/topic/beauty?page='

    FOOD_AND_DRINK = 'Food & Drink'
    FOOD_AND_DRINK_URL = 'https://www.thetimes.co.uk/topic/food-and-drink?page='

    FITNESS_AND_WELLBEING = 'Fitness & Wellbeing'
    FITNESS_AND_WELLBEING_URL = 'https://www.thetimes.co.uk/topic/fitness-and-wellbeing?page='

    HOME = 'Home'
    HOME_URL = 'https://www.thetimes.co.uk/topic/home-and-garden?page='

    GARDENING = 'Gardening'
    GARDENING_URL = 'https://www.thetimes.co.uk/topic/gardening?page='

    DRIVING = 'Driving'
    DRIVING_URL = 'https://www.thetimes.co.uk/topic/driving?page='


# TODO class Environment()
# article_links += browser.get_article_links('Environment', 'https://www.thetimes.co.uk/environment')


all_links = [(Business.SECTION, Business.ECONOMY), (Business.SECTION, Business.MARKETS),
             (Business.SECTION, Business.PROPERTY), (Business.SECTION, Business.PERSONAL_FINANCE),
             (Business.SECTION, Business.BANKING),

             (Society.SECTION, Society.HEALTH), (Society.SECTION, Society.SCIENCE),
             (Society.SECTION, Society.TECHNOLOGY), (Society.SECTION, Society.TRANSPORT),
             (Society.SECTION, Society.LAW),

             (Sport.SECTION, Sport.CRICKET), (Sport.SECTION, Sport.TENNIS), (Sport.SECTION, Sport.RUGBY_UNION),
             (Sport.SECTION, Sport.FORMULA_ONE), (Sport.SECTION, Sport.GOLF), (Sport.SECTION, Sport.RACING),
             (Sport.SECTION, Sport.BOXING), (Sport.SECTION, Sport.OLYMPICS),

             (ArtsAndCulture.SECTION, ArtsAndCulture.TV),
             (ArtsAndCulture.SECTION, ArtsAndCulture.FILM), (ArtsAndCulture.SECTION, ArtsAndCulture.MUSIC),
             (ArtsAndCulture.SECTION, ArtsAndCulture.RADIO_AND_PODCASTS),
             (ArtsAndCulture.SECTION, ArtsAndCulture.BOOKS), (ArtsAndCulture.SECTION, ArtsAndCulture.THEATRE),
             (ArtsAndCulture.SECTION, ArtsAndCulture.ART),

             (LifeAndStyle.SECTION, LifeAndStyle.BEAUTY), (LifeAndStyle.SECTION, LifeAndStyle.FOOD_AND_DRINK),
             (LifeAndStyle.SECTION, LifeAndStyle.FITNESS_AND_WELLBEING), (LifeAndStyle.SECTION, LifeAndStyle.HOME),
             (LifeAndStyle.SECTION, LifeAndStyle.GARDENING), (LifeAndStyle.SECTION, LifeAndStyle.DRIVING)
             ]
