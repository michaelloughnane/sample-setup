import sys
sys.path.append('michaelloughnane/sample-setup/src')
import fibonacci
from fibonacci import recur_fibo

def test_smallFib():
  assert recur_fibo(1) == 1, "Should be 1"
  
def test_bigFib():
  assert recur_fibo(100) == 354224848179261915075, "Should be 354224848179261915075"
