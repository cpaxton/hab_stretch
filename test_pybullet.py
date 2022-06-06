import pybullet as pb
import pybullet_data

client = pb.connect(pb.GUI)
# pb.setAdditionalSearchPath('.')
pb.setAdditionalSearchPath(pybullet_data.getDataPath())
pb.setGravity(0, 0, -9.8)

# Basic stuff here
plane_id = pb.loadURDF("plane.urdf")
start_pos = [0,0,1]
start_orn = pb.getQuaternionFromEuler([0,0,0])

# Load the stretch
robot_id = pb.loadURDF('./urdf/stretch.urdf', start_pos, start_orn)
