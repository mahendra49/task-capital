import unittest
import urllib.request
import json



SERVER_ON_HEROKU = "https://sample-python-app-task.herokuapp.com"


class Capitals(unittest.TestCase):
    

    #test to check if server is running
    def test_server(self): 
        res = urllib.request.urlopen(SERVER_ON_HEROKU)
        self.assertEqual(res.status ,200)

        

    """
    Test the route for get country capital
    This will contain test for both valid countries and invalid countries
    """

    def test_route_for_capital(self):

        """
        Test for these countries, here some are Valid countries and some are invalid
        And for corresponding indexs if country is valid then isValidCountry is True else False
        """

        countries  = [
                'India' , 'Italy' , '' , 
                'abra-ka-dabra' , 'Japan' , 
                'Malawi' , 'Youareawesome'
        ]

        isValidCountry = [
                False , False , True , 
                True , False , 
                False , True 
        ]

        for index , country in enumerate(countries):
            #print('http://localhost:5000/capital?country={}'.format(country))
            response = urllib.request.urlopen('{}/capital?country={}'.format(SERVER_ON_HEROKU,country))
            response = response.read().decode('utf-8')    #convert bytes stream into string
            response_status = json.loads(response)['error']  #if any error in response body then error field is True
            #print(response_status)
            self.assertEqual(response_status , isValidCountry[index]) 
        

if __name__ == '__main__':
    unittest.main()