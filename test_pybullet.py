import pybullet as pb
import pybullet_data
import time
from collections import namedtuple

client = pb.connect(pb.GUI)
# pb.setAdditionalSearchPath('.')
pb.setAdditionalSearchPath(pybullet_data.getDataPath())
pb.setGravity(0, 0, -9.8)

# Basic stuff here
plane_id = pb.loadURDF("plane.urdf")
start_pos = [0,0,0.1]
start_orn = pb.getQuaternionFromEuler([0, 0, -1.5607])

# Load the stretch
#robot_id = pb.loadURDF('./urdf/stretch.urdf', start_pos, start_orn)
robot_id = pb.loadURDF('./urdf/hab_stretch_dex_wrist_simplified.urdf', start_pos, start_orn)

# Get information about each joint
PbJointInfo = namedtuple('JointInfo', ['index', 'name', 'type', 'qindex', 'uindex', 'flags',
                                       'damping', 'friction', 'lower_limit', 'upper_limit',
                                       'max_force', 'max_velocity', 'link_name', 'axis',
                                       'parent_frame_pos', 'parent_frame_rot', 'parent_idx'])
num_joints = pb.getNumJoints(robot_id, client)
joint_infos = []
for i in range(num_joints):
    joint = PbJointInfo(*pb.getJointInfo(robot_id, i, client))
    joint_infos.append(joint)

    print(joint.index, joint.name, joint.link_name, joint.lower_limit, joint.upper_limit)

for i in range (10000):
    pb.stepSimulation()
    time.sleep(1./240.)
    pos, orn = pb.getBasePositionAndOrientation(robot_id)
    # Debug pose information as the robot falls over
    # print(pos, orn)
input("press enter to terminate")
pb.disconnect()
