import argparse
import os
import shutil
import subprocess


def edit_proc_card(proc_card_path, param_card_path, run_card_path, n_events):
    with open(proc_card_path, 'a') as f:
        # Turn pythia on for particle showering/hadronization.
        f.write('1\n0\n')
        # Read from the given cards and set the number of events.
        if param_card_path is not None:
            f.write('{}\n'.format(param_card_path))
        if run_card_path is not None:
            f.write('{}\n'.format(run_card_path))
        if n_events is not None:
            f.write('set nevents {}\n'.format(n_events))
        f.write('0\n')

def run_madgraph(proc_card_path, ufo_path, param_card_path=None, run_card_path=None, n_events=None):
    if ufo_path is not None:
        ufo_path = ufo_path.rstrip('/')
        ufo_dir = os.path.basename(ufo_path)
        shutil.copytree(ufo_path, 'madgraph/models/{}'.format(ufo_dir))
    proc_card_copy_path = os.path.join(os.getcwd(), 'proc_card.dat')
    shutil.copyfile(proc_card_path, proc_card_copy_path)
    edit_proc_card(proc_card_copy_path, param_card_path, run_card_path, n_events)
    subprocess.call(['/code/madgraph/bin/mg5_aMC', proc_card_copy_path])



def main():
    parser = argparse.ArgumentParser(description='Run madgraph+pythia.')
    parser.add_argument('proc_card', help='path to proc_card.')
    parser.add_argument('--ufo', help='path to UFO model directory.')
    parser.add_argument('--param_card', help='path to param_card.')
    parser.add_argument('--run_card', help='path to run_card.')
    parser.add_argument('--n_events', '-n', type=int, help='Number of events.')

    args = parser.parse_args()
    run_madgraph(args.proc_card, args.ufo, args.param_card, args.run_card, args.n_events)


if __name__ == '__main__':
    main()
