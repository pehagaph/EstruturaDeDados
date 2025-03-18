class BTreeNo
{
    private int valor;
    private BTreeNo esq;
    private BTreeNo dir;

    BTreeNo(int valor)
    {
        this.valor = valor;
    }

    public void setValor(int valor) { ... }
    public void setEsq(BTreeNo esq) { ... }
    public void setDir(BTreeNo dir) { ... }
    public int getValor() { ... }
    public BTreeNo getEsq() { ... }
    public BTreeNo getDir() { ... }
}


class BTree
{
    private BTreeNo raiz;

    private BTreeNo inserir(BTreeNo arvore, int novo)
    {
        BTreeNo aux = null;
        if (arvore == null)
        {
            aux.setValor(novo);
            return aux;
        }
        else if (novo < arvore.getValor())
            arvore.setEsq(inserir(arvore.getEsq(), novo));
        else
            arvore.setDir(inserir(arvore.getDir(), novo));

        return arvore;
    }

    public void inserirNo(int novo)
    {
        raiz = inserir(raiz, novo);
    }
}

public void exibirEsquerdo(BTreeNo arv)
{
    if (arv != null)
    {
        exibirEsquerdo(arv.getEsq());
        Console.WriteLine(arv.getValor());
    }
}

public void exibirDireito(BTreeNo arv)
{
    if (arv != null)
    {
        exibirDireito(arv.getEsq()); // Observação: Há um erro aqui, deveria ser arv.getDir()
        Console.WriteLine(arv.getValor());
    }
}

public void ExibirRaiz()
{
    Console.WriteLine("Raiz: " + raiz.getValor());
}

public void exibirNoEsq()
{
    exibirEsquerdo(raiz);
}

public void exibirNoDir()
{
    exibirDireito(raiz);
}

public void excluirNo(int item)
{
    BTreeNo aux = raiz, pai = null, filho = raiz, temp;
    while (aux != null && aux.getValor() != item)
    {
        pai = aux;
        if (item < aux.getValor())
            aux = aux.getEsq();
        else
            aux = aux.getDir();
    }

    if (aux == null)
    {
        Console.WriteLine("Valor não encontrado");
    }
    else if (aux.getDir() == null)
    {
        if (pai.getEsq() == aux)
            pai.setEsq(aux.getEsq());
        else
            pai.setDir(aux.getEsq());
    }
    else if (aux.getEsq() == null)
    {
        if (pai.getEsq() == aux)
            pai.setEsq(aux.getDir());
        else
            pai.setDir(aux.getDir());
    }
    else
    {
        if (pai == null)
        {
            if (aux.getDir() == null)
                raiz = aux.getEsq();
            else if (aux.getEsq() == null)
                raiz = aux.getDir();
            else
            {
                for (temp = aux, filho = aux.getEsq(); filho.getDir() != null; temp = filho, filho = filho.getDir());
                if (filho == aux.getEsq())
                {
                    temp.setDir(filho.getEsq());
                    filho.setEsq(raiz.getEsq());
                }
                filho.setDir(raiz.getDir());
                raiz = filho;
            }
        }
        else
        {
            for (temp = aux, filho = aux.getEsq(); filho.getDir() != null; temp = filho, filho = filho.getDir());
            if (filho != aux.getEsq())
            {
                temp.setDir(filho.getEsq());
                filho.setEsq(aux.getEsq());
            }
            filho.setDir(aux.getDir());
            if (pai.getEsq() == aux)
                pai.setEsq(filho);
            else
                pai.setDir(filho);
        }
    }
}
