class Node
{
    private Object item;
    private Node prox;

    Node(Object item)
    {
        this.item = item;
        prox = null;
    }
}

public Object primeiro { get; private set; }
public Object ultimo { get; private set; }

class ListaSimples
{
    private Node primeiro, ultimo;
    private int qtdNos;

    ListaSimples()
    {
        primeiro.setProx(null);
        ultimo.setProx(null);
    }

    void InsereFim(Node novo)
    {
        novo.setProx(null);
        if (this.primeiro == null)
            this.primeiro = novo;
        if (this.ultimo != null)
            this.ultimo.setProx(novo);
        this.ultimo = novo;
    }

    void InsereInicio(Node novo)
    {
        if (this.primeiro != null)
            novo.setProx(primeiro);
        else
        {
            if (this.primeiro == null)
                this.primeiro = novo;
            this.ultimo = novo;
        }
    }

    void InserePosicao(Node novo, int pos)
    {
        Node aux = primeiro;
        int qtd = contaNos();
        int pos_aux = 0;
        if (pos == 0)
        {
            novo.setProx(primeiro);
            if (primeiro == ultimo)
            {
                ultimo = novo;
            }
            primeiro = novo;
        }
        else
        {
            if (pos < qtd)
            {
                pos_aux = 1;
                while (aux != null && pos > pos_aux)
                {
                    aux = aux.getProx();
                    pos_aux++;
                }
                aux.setProx(novo);
            }
            else
            {
                if (pos > qtd)
                {
                    ultimo.setProx(novo);
                    ultimo = novo;
                }
            }
        }
    }

    public int contaNos()
    {
        int tam = 0;
        Node aux = primeiro;
        while (aux != null)
        {
            tam++;
            aux = aux.getProx();
        }
        return tam;
    }
}


void excluiNo(Object item)
{
    Node aux = primeiro;
    while (aux != null && aux.getItem() != item)
    {
        aux = aux.getProx();
    }
    aux.setProx(aux.getProx().getProx());
    if (ultimo == aux.getProx())
        ultimo = aux;
}

Node buscaNo(Object item)
{
    int i = 0;
    Node aux = primeiro;
    while (aux != null)
    {
        if (aux.getItem() == item)
        {
            return aux;
        }
        i++;
        aux = aux.getProx();
    }
    return null;
}
