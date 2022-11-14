from ete4.smartview import TreeStyle, NodeStyle, TreeLayout
from ete4.smartview  import RectFace, CircleFace, SeqMotifFace, TextFace, OutlineFace

#collapse in layout
#kingdom, phylum, class, order, family, genus, species, subspecies

def collapse_kingdom():
    def layout_fn(node):
        color = "red"
        if not node.is_root() and  node.props.get('rank') == 'superkingdom':
            face_name = TextFace(node.props.get('sci_name'), color=color)
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = color
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level1_kingdom"
    return layout_fn
    return

def collapse_phylum():
    def layout_fn(node):
        color="orange"
        if not node.is_root() and  node.props.get('rank') == 'phylum':
            face_name = TextFace(node.props.get('sci_name'), color=color)
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = color
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level2_phylum"
    return layout_fn
    return

def collapse_class():
    def layout_fn(node):
        color="yellow"
        if not node.is_root() and  node.props.get('rank') == 'class':
            face_name = TextFace(node.props.get('sci_name'), color=color)
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = color
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level3_class"
    return layout_fn
    return

def collapse_order():
    def layout_fn(node):
        color="green"
        if not node.is_root() and  node.props.get('rank') == 'order':
            face_name = TextFace(node.props.get('sci_name'), color=color)
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = color
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level4_order"
    return layout_fn
    return 

def collapse_family():
    def layout_fn(node):
        color="blue"
        if not node.is_root() and  node.props.get('rank') == 'family':
            face_name = TextFace(node.props.get('sci_name'), color=color)
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = color
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level5_family"
    return layout_fn
    return 

def collapse_genus():
    def layout_fn(node):
        color="indigo"
        if not node.is_root() and  node.props.get('rank') == 'genus':
            face_name = TextFace(node.props.get('sci_name'), color="indigo")
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = "indigo"
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level6_genus"
    return layout_fn
    return

def collapse_species():
    def layout_fn(node):
        if not node.is_root() and  node.props.get('rank') == 'species':
            face_name = TextFace(node.props.get('sci_name'), color="violet")
            node.sm_style["draw_descendants"] = False
            node.sm_style["outline_color"] = "violet"
            node.add_face(face_name, column = 8,  position = 'aligned', collapsed_only=True)
    layout_fn.name = "level7_species"
    return layout_fn
    return