# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:34:16 2016

@author: amundson
"""
import argparse
import spack

description  = "jfa prototype get command"

def setup_parser(subparser):
#    subparser.add_argument(
#        '-i', '--ignore-dependencies', action='store_true', dest='ignore_deps',
#        help="Do not try to install dependencies of requested packages.")
#    subparser.add_argument(
#        '-j', '--jobs', action='store', type=int,
#        help="Explicitly set number of make jobs.  Default is #cpus.")
#    subparser.add_argument(
#        '--keep-prefix', action='store_true', dest='keep_prefix',
#        help="Don't remove the install prefix if installation fails.")
#    subparser.add_argument(
#        '--keep-stage', action='store_true', dest='keep_stage',
#        help="Don't remove the build stage if installation succeeds.")
#    subparser.add_argument(
#        '-n', '--no-checksum', action='store_true', dest='no_checksum',
#        help="Do not check packages against checksum")
#    subparser.add_argument(
#        '-v', '--verbose', action='store_true', dest='verbose',
#        help="Display verbose build output while installing.")
#    subparser.add_argument(
#        '--fake', action='store_true', dest='fake',
#        help="Fake install.  Just remove the prefix and touch a fake file in it.")
    subparser.add_argument(
        'packages', nargs=argparse.REMAINDER, help="specs of packages to install")

def get(parser, args):
    if not args.packages:
        tty.die("get requires at least one package argument")

    specs = spack.cmd.parse_specs(args.packages, concretize=True)
    for spec in specs:
        print 'jfa spec:', spec
        print 'jfa spec.prefix:', spec.prefix
        for dep in spec.dependencies.values():
            print 'jfa dep:', dep
        print 'jfa: starting...\n\n'
        package = spack.db.get(spec)
        with spack.installed_db.write_transaction():
            package.do_get()
#        package = spack.db.get(spec)
#        with spack.installed_db.write_transaction():
#            package.do_install(
#                keep_prefix=args.keep_prefix,
#                keep_stage=args.keep_stage,
#                ignore_deps=args.ignore_deps,
#                make_jobs=args.jobs,
#                verbose=args.verbose,
#                fake=args.fake)
