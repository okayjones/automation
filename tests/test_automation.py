import pytest
from automation import __version__
from automation.automation import scrape_phone_numbers, scrape_email

def test_version():
    assert __version__ == '0.1.0'

def test_scrape_phone_numbers(text):
    actual = scrape_phone_numbers(text)
    expected = '048-736-2919\n178-383-0937'
    assert actual == expected

def test_scrape_email(text):
    actual = scrape_email(text)
    expected = 'danielletaylor@hotmail.com\ndeleonchristopher@christian-wilson.com'
    assert actual == expected
 
@pytest.fixture
def text():
    return "One world we cold public trip. Tonight stock two short financial million. Cost some animal great course next eye. danielletaylor@hotmail.com Less or information clear century guess somebody. Sister follow wide report land find.861-26-5898Especially can south wall need.+1-178-383-0937x54779He final hour painting nature people never rise. Home decide ever kind together dinner. danielletaylor@hotmail.com +1-178-383-0937x54779Thank appear test call in key set. Approach agree land him gas alone reach. Agent region book whose military traditional quite. My evidence little those minute pick approach crime. Compare reflect measure by kind risk boy recently. deleonchristopher@christian-wilson.com Tv career but foot foot actually rise. Type once hot answer.766-91-8057Difference them son born cup probably.001-048-736-2919Much across whether soldier minute. Enough able expect edge these training hit."
