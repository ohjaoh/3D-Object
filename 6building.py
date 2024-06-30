import bpy

def create_building(name, width, depth, height, location):
    # 건물 기본 큐브 생성
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(location[0], location[1], location[2] + height / 2))
    building = bpy.context.object
    building.name = name
    building.scale = (width / 2, depth / 2, height / 2)
    
    # 창문 구멍 생성
    create_front_back_windows(building, width, depth, height)
    create_side_windows(building, width, depth, height)

def create_front_back_windows(building, width, depth, height):
    window_height = 15  # 창문 높이
    window_width = 20   # 창문 너비 
    window_depth = 4    # 구멍의 깊이
    floor_height = 30   # 각 층의 높이
    num_floors = 5      # 층 수
    gap_between_windows = 10  # 창문 사이의 간격

    # 각 층의 높이를 계산하여 창문을 배치
    for floor in range(num_floors):
        z = floor * floor_height + floor_height / 2
        x_start = -width / 2 + 10
        while x_start < width / 2 - window_width - 10:
            # 전면 (Front) 창문 구멍 생성
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, 
                                            location=(x_start + window_width / 2, depth / 2 - window_depth / 2, z))
            window_hole = bpy.context.object
            window_hole.scale = (window_width / 2, window_depth / 2, window_height / 2)
            apply_boolean_modifier(building, window_hole)

            # 후면 (Back) 창문 구멍 생성
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, 
                                            location=(x_start + window_width / 2, -depth / 2 + window_depth / 2, z))
            window_hole = bpy.context.object
            window_hole.scale = (window_width / 2, window_depth / 2, window_height / 2)
            apply_boolean_modifier(building, window_hole)

            x_start += window_width + gap_between_windows

def create_side_windows(building, width, depth, height):
    window_height = 20  # 창문 높이
    window_width = 40   # 창문 너비
    window_depth = 3    # 구멍의 깊이
    floor_height = 30   # 각 층의 높이
    num_floors = 5      # 층 수
    gap_between_windows = 10  # 창문 사이의 간격

    # 각 층의 높이를 계산하여 창문을 배치
    for floor in range(num_floors):
        z = floor * floor_height + floor_height / 2
        y_start = -depth / 2 + 10
        while y_start < depth / 2 - window_width - 10:
            # 좌측면 (Left) 창문 구멍 생성
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, 
                                            location=(width / 2 - window_depth / 2, y_start + window_width / 2, z))
            window_hole = bpy.context.object
            window_hole.scale = (window_depth / 2, window_width / 2, window_height / 2)
            apply_boolean_modifier(building, window_hole)

            # 우측면 (Right) 창문 구멍 생성
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, 
                                            location=(-width / 2 + window_depth / 2, y_start + window_width / 2, z))
            window_hole = bpy.context.object
            window_hole.scale = (window_depth / 2, window_width / 2, window_height / 2)
            apply_boolean_modifier(building, window_hole)

            y_start += window_width + gap_between_windows

def apply_boolean_modifier(building, window_hole):
    # 부울 수정자를 이용하여 창문 구멍을 건물에서 잘라내기
    bpy.context.view_layer.objects.active = building
    bool_mod = building.modifiers.new(name="Boolean", type='BOOLEAN')
    bool_mod.operation = 'DIFFERENCE'
    bool_mod.object = window_hole
    bpy.ops.object.modifier_apply(modifier=bool_mod.name)
    
    # 창문 구멍 제거
    bpy.data.objects.remove(window_hole)

# 5번 건물 생성
#create_building("Building_5", 50, 220, 150, (0, 0, 0))

# 두 건물 사이의 간격 설정
gap = 10

# 6번 건물 생성, x 위치에 5번 건물의 x 길이와 간격을 더하여 위치 지정
create_building("Building_6", 50, 175, 150, (0, 0, 0))
