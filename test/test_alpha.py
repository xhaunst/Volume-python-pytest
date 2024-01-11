from src.Volume import *

def test_one():
  assert Box(5,2,2) == 20
  assert Box(2,1,2) == 4
  assert Pyramid(5,2,2) == (5*2*2)/3
  assert Pyramid(2,3,4) == (2*3*4)/3
