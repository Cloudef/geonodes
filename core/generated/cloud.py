from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Cloud(Socket):

    def domain_size(self):
        """ > Method <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'POINTCLOUD'

        Returns
        -------
        - node [point_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='POINTCLOUD')
        return node

    @classmethod
    def DistributeingridDensityRandom(cls, grid=None, density=None, seed=None):
        """ > Constructor <&Node Distribute Points in Grid>

        Information
        -----------
        - Parameter 'mode' : 'DENSITY_RANDOM'

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Density': density, 'Seed': seed}, mode='DENSITY_RANDOM')
        return cls(node._out)

    @classmethod
    def DistributeingridDensityGrid(cls, grid=None, spacing=None, threshold=None):
        """ > Constructor <&Node Distribute Points in Grid>

        Information
        -----------
        - Parameter 'mode' : 'DENSITY_GRID'

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - spacing (Vector) : socket 'Spacing' (id: Spacing)
        - threshold (Float) : socket 'Threshold' (id: Threshold)

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Spacing': spacing, 'Threshold': threshold}, mode='DENSITY_GRID')
        return cls(node._out)

    @classmethod
    def DistributeInGrid(cls, grid=None, density=None, seed=None, mode='DENSITY_RANDOM'):
        """ > Constructor <&Node Distribute Points in Grid>

        Arguments
        ---------
        - grid (Float) : socket 'Grid' (id: Grid)
        - density (Float) : socket 'Density' (id: Density)
        - seed (Integer) : socket 'Seed' (id: Seed)
        - mode (str): parameter 'mode' in ('DENSITY_RANDOM', 'DENSITY_GRID')

        Returns
        -------
        - Cloud
        """
        node = Node('Distribute Points in Grid', sockets={'Grid': grid, 'Density': density, 'Seed': seed}, mode=mode)
        return cls(node._out)

    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Method <&Node Instance on Points>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instance (Geometry) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', sockets={'Points': self, 'Selection': self._sel, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def interpolate_curves(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Method <&Node Interpolate Curves>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - guide_curves (Geometry) : socket 'Guide Curves' (id: Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve [closest_index_ (Integer), closest_weight_ (Float)]
        """
        node = Node('Interpolate Curves', sockets={'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': self, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return node._out

    @classmethod
    def Points(cls, count=None, position=None, radius=None):
        """ > Constructor <&Node Points>

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Points', sockets={'Count': count, 'Position': position, 'Radius': radius})
        return cls(node._out)

    def to_curves(self, curve_group_id=None, weight=None):
        """ > Method <&Node Points to Curves>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - curve_group_id (Integer) : socket 'Curve Group ID' (id: Curve Group ID)
        - weight (Float) : socket 'Weight' (id: Weight)

        Returns
        -------
        - Curve
        """
        node = Node('Points to Curves', sockets={'Points': self, 'Curve Group ID': curve_group_id, 'Weight': weight})
        return node._out

    def to_sdf_grid(self, radius=None, voxel_size=None):
        """ > Method <&Node Points to SDF Grid>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - voxel_size (Float) : socket 'Voxel Size' (id: Voxel Size)

        Returns
        -------
        - Float
        """
        node = Node('Points to SDF Grid', sockets={'Points': self, 'Radius': radius, 'Voxel Size': voxel_size})
        return node._out

    def to_vertices(self):
        """ > Method <&Node Points to Vertices>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Mesh
        """
        node = Node('Points to Vertices', sockets={'Points': self, 'Selection': self._sel})
        return node._out

    def to_volume(self, density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """ > Method <&Node Points to Volume>

        Information
        -----------
        - Socket 'Points' : self

        Arguments
        ---------
        - density (Float) : socket 'Density' (id: Density)
        - voxel_amount (Float) : socket 'Voxel Amount' (id: Voxel Amount)
        - radius (Float) : socket 'Radius' (id: Radius)
        - resolution_mode (str): parameter 'resolution_mode' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

        Returns
        -------
        - Volume
        """
        node = Node('Points to Volume', sockets={'Points': self, 'Density': density, 'Voxel Amount': voxel_amount, 'Radius': radius}, resolution_mode=resolution_mode)
        return node._out

    @property
    def radius(self):
        """ Property get node <Node Set Point Radius>
        """
        return Node('Radius', sockets={})._out

    @radius.setter
    def radius(self, radius=None):
        """ > Jump Method <&Node Set Point Radius>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Set Point Radius', sockets={'Points': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

