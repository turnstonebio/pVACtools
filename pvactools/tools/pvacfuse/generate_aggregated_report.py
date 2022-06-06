import sys
import argparse
import tempfile

from pvactools.lib.aggregate_all_epitopes import UnmatchedSequenceAggregateAllEpitopes

def define_parser():
    parser = argparse.ArgumentParser(
        "pvacfuse generate_aggregated_report",
        description="Generate an aggregated report from a pVACfuse .all_epitopes.tsv report file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "input_file",
        help="A pVACfuse .all_epitopes.tsv report file"
    )
    parser.add_argument(
        "output_file",
        help="The file path to write the aggregated report tsv to"
    )
    parser.add_argument(
        '-b', '--binding-threshold', type=int,
        help="Tier epitopes in the \"Pass\" tier when the mutant allele "
             + "has ic50 binding scores below this value and in the \"Relaxed\" tier when the mutation allele has ic50 binding scores below double this value.",
        default=500
    )

    return parser

def main(args_input = sys.argv[1:]):
    parser = define_parser()
    args = parser.parse_args(args_input)

    tmp_fh = tempfile.NamedTemporaryFile()

    print("Creating Aggreggated Report")
    UnmatchedSequenceAggregateAllEpitopes(args.input_file, args.output_file, binding_threshold=args.binding_threshold).execute()
    print("Completed")

if __name__ == '__main__':
    main()
