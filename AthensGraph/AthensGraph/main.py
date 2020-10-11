import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

acropolis = 'Acropolis'
acropolis_museum = 'Acropolis Museum'
national_archaeology_Museum = 'National Archaeology Museum'
plaka = 'Pláka'

G.add_nodes_from([acropolis, acropolis_museum, national_archaeology_Museum])

G.add_edges_from([(acropolis, acropolis_museum), (acropolis, national_archaeology_Museum), (plaka, acropolis)])

# G = nx.petersen_graph()

options = {
    # 'node_color': 'black',
    # 'node_size': 120,
    'width': 3,
    'with_labels': True,
    'font_weight': 'bold',
}

plt.subplot(121)
nx.draw(G, **options)

plt.show()
