from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'text',
            default_value='Hola mundo',
            description='Texto a republicar'
        ),

        ExecuteProcess(
            cmd=['/home/user/.local/bin/republisher_server'],
            output='screen'
        ),

        ExecuteProcess(
            cmd=[
                '/home/user/.local/bin/republisher_client',
                LaunchConfiguration('text')
            ],
            output='screen'
        )
    ])
