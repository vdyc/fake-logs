# pylint: disable=C0103
import argparse
from fake_logs.fake_logs    import FakeLogs
from fake_logs.line_pattern import LinePattern


parser = argparse.ArgumentParser(description="Fake logs")
parser.add_argument("--Output"      , "-o", dest="output"      , help="output destination (.gz extension supported, STDOUT if not provided)" , type=str)
parser.add_argument("--Num"         , "-n", dest="num_lines"   , help="Number of lines to generate (0 for infinite)", type=int, default=10)
parser.add_argument("--Sleep"       , "-s", dest="sleep"       , help="Sleep this long between lines (in seconds)"  , type=float, default=None)
parser.add_argument("--Format"      , "-f", dest="format"      , help="Line format", choices=["apache", "nginx", "lighttpd", "elf", "clf", "ncsa", "logcat"], type=str, default="logcat")
parser.add_argument("--Pattern"     , "-p", dest="pattern"     , help="Custom pattern", type=str, default=None)
parser.add_argument("--Date-pattern", "-d", dest="date_pattern", help="Date pattern", type=str, default=None)
parser.add_argument("--Log-freq",     "-l", dest="log_freq"    , help="recurrence in one minute", type=int, default=15000)
parser.add_argument("--Realtime",     "-r", dest="realtime"    , help="log interval with real time sleep", type=bool, default=False)
args = parser.parse_args()


def run_from_cli(fake_tokens=None):
	"""Parse command-line options and run 'Fake Logs'."""
	line_pattern = LinePattern(args.pattern, date_pattern=args.date_pattern, file_format=args.format, fake_tokens=fake_tokens, log_freq=args.log_freq)
	FakeLogs(
		filename=args.output,
		num_lines=args.num_lines,
		sleep=args.sleep,
		line_pattern=line_pattern,
		file_format=args.format,
		real_time=args.realtime,
	).run()
