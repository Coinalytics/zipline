#
# Copyright 2014 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
import pytz, Quandl
from pprint import pprint
from zipline import TradingAlgorithm
from zipline.utils.factory import load_from_yahoo
from zipline.api import order


def initialize(context):
    context.number = 10


def handle_date(context, data):
    order('BITCOIN', context.number)
    print "Ordering " + str(context.number) + " Bitcoins at "
    pprint(context)
    print "Data for context:"
    pprint(data)
    #print(context.test)


if __name__ == '__main__':
    import pylab as pl
    #start = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
    #end = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)
    start = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
    end = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)
    data = load_from_yahoo(stocks=['AAPL'], indexes={}, start=start,
                           end=end)

    print "Apple:"
    print data

    print "Bitcoin:"
    #data = Quandl.get('BITCOIN/BITSTAMPUSD', authtoken='pG7ffySvtgWpftzDyipk',
    #    trim_start=start, trim_end=end, 
        #collapse='daily',
        #transformation='rdiff', 
        #rows=400, 
        #returns='numpy'
    #    )
    #print data


#if trading, execute this code:
    # clean outliers from the data
    data = data.dropna()
    algo = TradingAlgorithm(initialize=initialize,
                            handle_data=handle_date)
    results = algo.run(data)
    
    print results

    results.portfolio_value.plot()
    pl.show()
