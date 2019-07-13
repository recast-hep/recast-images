import argparse
import os
import shutil
import subprocess


def edit_proc_card(proc_card_path, param_card_path, run_card_path, n_events):
    with open(proc_card_path, 'a') as f:
        # Turn pythia on for particle showering/hadronization.
        f.write('1\n0\n')
        # Read from the given cards and set the number of events.
        if param_card_path is not None and param_card_path != "default":
            f.write('{}\n'.format(param_card_path))
        if run_card_path is not None and run_card_path != "default":
            f.write('{}\n'.format(run_card_path))
        if n_events is not None:
            f.write('set nevents {}\n'.format(n_events))
        f.write('0\n')


def run_madgraph(proc_card_path, output_path, ufotar, param_card_path=None, run_card_path=None, n_events=None):
    if ufotar is not None:
        if '/' in ufotar:
            ufo_name, ufo_ext = os.path.splitext(os.path.basename(ufotar))
        else:
            ufo_name, ufo_ext = os.path.splitext(ufotar)
        assert ufo_ext == '.tar', 'ufo must be a tar file!'
        subprocess.call(['tar', '-xvf', ufotar])
        shutil.copytree(ufo_name, 'madgraph/models/{}'.format(ufo_name))
    proc_card_copy_path = os.path.join(os.getcwd(), 'proc_card.dat')
    shutil.copyfile(proc_card_path, proc_card_copy_path)
    edit_proc_card(proc_card_copy_path, param_card_path,
                   run_card_path, n_events)
    subprocess.call(['/code/madgraph/bin/mg5_aMC', proc_card_copy_path])
    run_dir = os.path.join(os.getcwd(), 'PROC_sm_0', 'Events', 'run_1')
    subprocess.call(['gunzip', os.path.join(
        run_dir, 'tag_1_pythia8_events.hepmc.gz')])
    subprocess.call(['sudo', 'cp', os.path.join(
        run_dir, 'tag_1_pythia8_events.hepmc'), output_path])


def main():
    parser = argparse.ArgumentParser(description='Run madgraph+pythia.')
    parser.add_argument('proc_card', help='path to proc_card.')
    parser.add_argument('output', help='path for output hepmc.')
    parser.add_argument('--ufotar', help='path to UFO tar file.')
    parser.add_argument(
        '--param_card', help='path to param_card. Leave unspecified or pass "default" to use the default param card for the model.')
    parser.add_argument(
        '--run_card', help='path to run_card. Leave unspecified or pass "default" to use the default run card for the model.')
    parser.add_argument('--n_events', '-n', type=int, help='Number of events.')

    args = parser.parse_args()
    run_madgraph(args.proc_card, args.output, args.ufotar,
                 args.param_card, args.run_card, args.n_events)


if __name__ == '__main__':
    main()
