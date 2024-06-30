from pygltflib import GLTF2, Animation, AnimationChannel, AnimationSampler

# GLB 파일 불러오기
file_path = 'C:\\Users\\user\\Desktop\\bus\\bus_anime.glb'
model = GLTF2().load(file_path)

# 새 애니메이션 객체 생성
merged_animation = Animation()
merged_animation.channels = []
merged_animation.samplers = []

# 모든 애니메이션의 채널과 샘플러 병합
for animation in model.animations:
    for channel in animation.channels:
        new_channel = AnimationChannel(
            sampler=len(merged_animation.samplers) + animation.channels.index(channel),
            target=channel.target
        )
        merged_animation.channels.append(new_channel)

    for sampler in animation.samplers:
        new_sampler = AnimationSampler(
            input=sampler.input,
            output=sampler.output,
            interpolation=sampler.interpolation
        )
        merged_animation.samplers.append(new_sampler)

# 기존 애니메이션 제거하고 병합된 애니메이션 추가
model.animations = [merged_animation]

# 병합된 애니메이션 정보 출력
print(f"Combined Animation: {len(merged_animation.channels)} channels, {len(merged_animation.samplers)} samplers")

for index, channel in enumerate(merged_animation.channels):
    print(f"Channel {index}: target node {channel.target.node}, path {channel.target.path}")

for index, sampler in enumerate(merged_animation.samplers):
    print(f"Sampler {index}: input {sampler.input}, output {sampler.output}")

# 병합된 GLB 파일 저장
output_path = 'C:\\Users\\user\\Desktop\\bus_combined.glb'
model.save_binary(output_path)
