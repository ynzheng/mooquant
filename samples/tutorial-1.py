from mooquant import strategy
from mooquant.barfeed import yahoofeed


class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(MyStrategy, self).__init__(feed)
        self.__instrument = instrument

    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())

if __name__ == '__main__':
	
	# Load the yahoo feed from the CSV file
	feed = yahoofeed.Feed()
	feed.addBarsFromCSV("orcl", "../tests/data/orcl-2000.csv")

	# Evaluate the strategy with the feed's bars.
	strat = MyStrategy(feed, "orcl")
	strat.run()