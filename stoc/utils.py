import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode()
    buffer.close()
    return graph


def pur_plot(x, y):
    plt.switch_backend("AGG")
    plt.xticks(rotation=35)
    plt.title('Purchase Graph')
    plt.xlabel('Dates')
    plt.ylabel('Amount')
    plt.plot(x, y, '*--')
    plt.tight_layout()
    plt.grid()
    graph = get_graph()
    return graph

def sal_plot(p, q):
    plt.switch_backend("AGG")
    plt.xticks(rotation=35)
    plt.title('Sales Graph')
    plt.xlabel('Dates')
    plt.ylabel('Amount')
    plt.plot(p, q, '*--')
    plt.tight_layout()
    plt.grid()
    graph = get_graph()
    return graph

def ex_plot(a, b):
    plt.switch_backend("AGG")
    plt.xticks(rotation=35)
    plt.title('Expences Graph')
    plt.xlabel('Dates')
    plt.ylabel('Amount')
    plt.plot(a, b, '*--')
    plt.tight_layout()
    plt.grid()
    graph = get_graph()
    return graph