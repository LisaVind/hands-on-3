import md
import sys
import os

md.run_md()


if not os.path.exists('cu.traj'):
    sys.exit(1)
