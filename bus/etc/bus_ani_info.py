from pygltflib import GLTF2
import os

# GLB 파일 불러오기
file_path = 'C:\\Users\\user\\Desktop\\bus\\bus_anime.glb'

# 파일 존재 여부 확인
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    model = GLTF2().load(file_path)

    # 애니메이션 정보 추출
    animation_info = []

    for anim_index, animation in enumerate(model.animations):
        channels = len(animation.channels)
        samplers = len(animation.samplers)
        animation_info.append({
            "animation_index": anim_index,
            "channels": channels,
            "samplers": samplers
        })

    # 애니메이션 정보 출력
    for info in animation_info:
        print(f"Animation {info['animation_index']}: {info['channels']} channels, {info['samplers']} samplers")
