from convex_hull_by_hana import myConvexHull
from convex_hull_by_hana import fungsi_convex_hull_atas
from convex_hull_by_hana import membuat_area

import numpy as np
tes = [np.array([1,2]), np.array([4,3]), np.array([4,6])]
print(fungsi_convex_hull_atas(np.array([0,0]),np.array([5,5]), tes))
