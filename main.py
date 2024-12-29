import sys
from usecase.simulate import simulated_transactions

try:
    while True:
        simulated_transactions()
except KeyboardInterrupt:
    sys.stderr.write('Aborted by user\n')