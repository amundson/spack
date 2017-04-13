##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
import argparse

import llnl.util.tty as tty
import spack
import spack.cmd

description = "Export stage information for package"


def setup_parser(subparser):
    subparser.add_argument(
        'spec', help="spec of package to stage")

def export_stage(parser, args):
    specs = spack.cmd.parse_specs([args.spec], concretize=True)
    spec = specs[0]
    package = spack.repo.get(spec)
    fetcher = package.fetcher[0]
    print(fetcher.__class__.__name__)
    the_dict = fetcher.__dict__
    literal_eval_types = [type(''), type(None), type([]), type(()), type(1.0), type(0), type(True)]
    scrubbed_dict = {key:(the_dict[key] if type(the_dict[key]) in literal_eval_types else '_non_l_e_t') for key in the_dict.keys()}
    print(scrubbed_dict)
