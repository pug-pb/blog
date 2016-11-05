Principais elementos da sintaxe Markdown
========================================

Fonte: http://daringfireball.net/projects/markdown/syntax

Excertos e tradução: @hilam

### ELEMENTOS DE BLOCO

#### PARÁGRAFOS E QUEBRAS DE LINHA

Um parágrafo é simplesmente uma ou mais linhas consecutivas de texto, separadas
por uma ou mais linhas em branco. (Uma linha em branco é qualquer uma que pareça
com uma linha em branco - uma linha contendo apenas espaços em branco ou tabulações
é considerada em branco.) Parágrafos não devem ser identados com espaços ou tabulações.

#### CABEÇALHOS


    Isto é um H1
    ============

    Isto é um H2
    ------------

produz:

Isto é um H1
============

Isto é um H2
------------

Qualquer número de =’s ou -’s funcionará.

Outra forma:

    # Isto é um H1

    ## Isto é um H2

    ###### Isto é um H6

# Isto é um H1

## Isto é um H2

###### Isto é um H6


#### CITAÇÕES

Markdown usa o caractere >, como no estilo email, para citações. Se você costuma
citar passagens de emails, então você saberá criar uma citação em Markdown. Ele
fica melhor se você distribui o texto e põe o caractere > antes de cada linha:

    > Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
    > consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    > Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
    >
    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    > id sem consectetuer libero luctus adipiscing.

> Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
>
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

É possível colocar o > apenas no início da primeira linha do parágrafo citado:

    > Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
    consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
    Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

    > Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
    id sem consectetuer libero luctus adipiscing.

> Esta é uma citação com dois parágrafos. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

Citações podem ser aninhadas (por ex.: uma citação dentro da citação) adicionando
o caractere > para dicionar níveis:

    > Primeiro nível da citação.
    >
    > > Citação aninhada, num segundo nível.
    >
    > De volta ao primeiro nível da citação.

> Primeiro nível da citação.
>
> > Citação aninhada, num segundo nível.
>
> De volta ao primeiro nível da citação.

Citações podem conter outros elementos Markdown elements, incluindo cabeçalhos,
 listas, e blocos de código:

    > ## Cabeçalho H2
    >
    > 1.   Primeiro item da lista.
    > 2.   Segundo item.
    >
    > Um exemplo com código:
    >
    >     return shell_exec("echo $input | $markdown_script");

> ## Cabeçalho H2
>
> 1.   Primeiro item da lista.
> 2.   Segundo item.
>
> Um exemplo com código:
>
>     return shell_exec("echo $input | $markdown_script");


#### LISTAS

Markdown suporta listas ordenadas (numeradas) e não ordenadas (bullet).

Listas não ordenadas usam *, + e - (não misturados):

    *   Red
    *   Green
    *   Blue

equivalente a:

    +   Red
    +   Green
    +   Blue

e:

    -   Red
    -   Green
    -   Blue

todos produzem:

*   Red
*   Green
*   Blue

Listas ordenadas usam números seguidos de ponto(.):

    1.  Bird
    2.  McHale
    3.  Parish

1.  Bird
2.  McHale
3.  Parish

Outros exemplos:

    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
        Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
        viverra nec, fringilla in, laoreet vitae, risus.
    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
        Suspendisse id sem consectetuer libero luctus adipiscing.

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

Mas se você for preguiçoso, não precisa:

    *   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
    *   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.

Os itens da lista podem consistir de vários parágrafos. Cada parágrafo
subsequente no item da lista deve ser identado por 4 espaços ou tabulação:

    1.  Um item de lista com dois parágrafos. Lorem ipsum dolor
        sit amet, consectetuer adipiscing elit. Aliquam hendrerit
        mi posuere lectus.

        Vestibulum enim wisi, viverra nec, fringilla in, laoreet
        vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
        sit amet velit.

    2.  Suspendisse id sem consectetuer libero luctus adipiscing.

1.  Um item de lista com dois parágrafos. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

        *   Item de lista com dois parágrafos.

            Segundo parágrafo do item. Só
        é necessário identar a primeira linha. Lorem ipsum dolor
        sit amet, consectetuer adipiscing elit.

        *   Outro item da lista.

*   Item de lista com dois parágrafos.

    Segundo parágrafo do item. Só
é necessário identar a primeira linha. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

*   Outro item da lista.

É possível indicar uma lista ordenada por acidente, escrevendo algo como isso:

    1986. Que grande temporada.

1986. Que grande temporada.

Em outras palavras, uma sequência número-ponto-espaço no começo de uma linha.
Para evitar isso, você pode "escapar" o ponto(.) com a barra invertida:

    1986\. Que grande temporada.

1986\. Que grande temporada.


#### BLOCOS DE CÓDIGO

Para produzir um bloco de código, simplesmente idente cada linha do bloco com,
pelo menos, 4 espaços ou 1 tabulação:

    Parágrafo normal.

        Bloco de código.

Markdown vai gerar:

Parágrafo normal.

    Bloco de código.

Exemplo com Python:

    def teste():
        return "Hello PUG!"

    teste()

Um bloco de código continua até atingir uma linha que não está identada.


    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

Sintaxe regular do Markdown não é processada dentro de blocos de código.


#### RÉGUAS HORIZONTAIS (HR)

É possível produzir uma régua horizontal colocando três ou mais hífens,
asteriscos ou sublinhados numa linha.

    * * *

    ***

    *****

    - - -

    ---------------------------------------

* * *

***

*****

- - -

---------------------------------------


#### LINKS

Markdown suporta dois estilos de links: inline e reference.

Em ambos, o texto do link é delimitado por [colchetes].

Para criar um link "inline", use um conjunto de parêntesis imediatamente após
o colchete que finaliza o texto do link. Dentro dos parêntesis, coloque a URL,
com um título opcional para o link, esntre aspas. Por exemplo:

    Este é [um exemplo](http://example.com/ "Título") de link inline.

    [Este link](http://example.net/) não tem o atributo título.

Este é [um exemplo](http://example.com/ "Título") de link inline.

[Este link](http://example.net/) não tem o atributo título.

Podem ser usados caminhos relativos:

    Veja minha página [Sobre](/about/) para detalhes.

Veja minha página [Sobre](/about/) para detalhes.

Links estilo "reference" usam um segundo conjunto de colchetes, dentro dos quais
colocamos um "label" de nossa escolha para identificar o link:

    Isto é [um exemplo][id] de link estilo "reference".

Isto é [um exemplo][id] de link estilo "reference".

Pode-se, opcionalmente, usar um espaço para separar os conjuntos de colchetes:

    Este é [um exemplo] [id] de link estilo "reference".

Este é [um exemplo] [id] de link estilo "reference".

Então, em qualquer lugar do documento, você define o "label" do seu link assim:

    [id]: http://example.com/  "Título Opcional aqui"

[id]: http://example.com/  "Título Opcional aqui"

The link URL may, optionally, be surrounded by angle brackets:

[id]: <http://example.com/>  "Optional Title Here"
You can put the title attribute on the next line and use extra spaces or tabs for padding, which tends to look better with longer URLs:

[id]: http://example.com/longish/path/to/resource/here
    "Optional Title Here"
Link definitions are only used for creating links during Markdown processing, and are stripped from your document in the HTML output.

Link definition names may consist of letters, numbers, spaces, and punctuation — but they are not case sensitive. E.g. these two links:

[link text][a]
[link text][A]
are equivalent.

The implicit link name shortcut allows you to omit the name of the link, in which case the link text itself is used as the name. Just use an empty set of square brackets — e.g., to link the word “Google” to the google.com web site, you could simply write:

[Google][]
And then define the link:

[Google]: http://google.com/
Because link names may contain spaces, this shortcut even works for multiple words in the link text:

Visit [Daring Fireball][] for more information.
And then define the link:

[Daring Fireball]: http://daringfireball.net/
Link definitions can be placed anywhere in your Markdown document. I tend to put them immediately after each paragraph in which they’re used, but if you want, you can put them all at the end of your document, sort of like footnotes.

Here’s an example of reference links in action:

I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"
Using the implicit link name shortcut, you could instead write:

I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

  [google]: http://google.com/        "Google"
  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
  [msn]:    http://search.msn.com/    "MSN Search"
Both of the above examples will produce the following HTML output:

<p>I get 10 times more traffic from <a href="http://google.com/"
title="Google">Google</a> than from
<a href="http://search.yahoo.com/" title="Yahoo Search">Yahoo</a>
or <a href="http://search.msn.com/" title="MSN Search">MSN</a>.</p>
For comparison, here is the same paragraph written using Markdown’s inline link style:

I get 10 times more traffic from [Google](http://google.com/ "Google")
than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or
[MSN](http://search.msn.com/ "MSN Search").
The point of reference-style links is not that they’re easier to write. The point is that with reference-style links, your document source is vastly more readable. Compare the above examples: using reference-style links, the paragraph itself is only 81 characters long; with inline-style links, it’s 176 characters; and as raw HTML, it’s 234 characters. In the raw HTML, there’s more markup than there is text.

With Markdown’s reference-style links, a source document much more closely resembles the final output, as rendered in a browser. By allowing you to move the markup-related metadata out of the paragraph, you can add links without interrupting the narrative flow of your prose.

#### ÊNFASE

Asteriscos (*) e sublinhados (_) são indicadores de ênfase.

    *um asterisco*

    _um sublinhado_

    **dois asteriscos**

    __dois sublinhados__

produzirão:

*um asterisco*

_um sublinhado_

**dois asteriscos**

__dois sublinhados__


#### CODE

To indicate a span of code, wrap it with backtick quotes (`). Unlike a pre-formatted code block, a code span indicates code within a normal paragraph. For example:

Use the `printf()` function.
will produce:

<p>Use the <code>printf()</code> function.</p>

To include a literal backtick character within a code span, you can use multiple backticks as the opening and closing delimiters:

``There is a literal backtick (`) here.``
which will produce this:

<p><code>There is a literal backtick (`) here.</code></p>
The backtick delimiters surrounding a code span may include spaces — one after the opening, one before the closing. This allows you to place literal backtick characters at the beginning or end of a code span:

A single backtick in a code span: `` ` ``

A backtick-delimited string in a code span: `` `foo` ``
will produce:

<p>A single backtick in a code span: <code>`</code></p>

<p>A backtick-delimited string in a code span: <code>`foo`</code></p>
With a code span, ampersands and angle brackets are encoded as HTML entities automatically, which makes it easy to include example HTML tags. Markdown will turn this:

Please don't use any `<blink>` tags.
into:

<p>Please don't use any <code>&lt;blink&gt;</code> tags.</p>
You can write this:

`&#8212;` is the decimal-encoded equivalent of `&mdash;`.
to produce:

<p><code>&amp;#8212;</code> is the decimal-encoded
equivalent of <code>&amp;mdash;</code>.</p>
IMAGES

Admittedly, it’s fairly difficult to devise a “natural” syntax for placing images into a plain text document format.

Markdown uses an image syntax that is intended to resemble the syntax for links, allowing for two styles: inline and reference.

Inline image syntax looks like this:

![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")
That is:

An exclamation mark: !;
followed by a set of square brackets, containing the alt attribute text for the image;
followed by a set of parentheses, containing the URL or path to the image, and an optional title attribute enclosed in double or single quotes.
Reference-style image syntax looks like this:

![Alt text][id]
Where “id” is the name of a defined image reference. Image references are defined using syntax identical to link references:

[id]: url/to/image  "Optional title attribute"
As of this writing, Markdown has no syntax for specifying the dimensions of an image; if this is important to you, you can simply use regular HTML <img> tags.

### MISCELLANEOUS

#### AUTOMATIC LINKS

Markdown supports a shortcut style for creating “automatic” links for URLs and email addresses: simply surround the URL or email address with angle brackets. What this means is that if you want to show the actual text of a URL or email address, and also have it be a clickable link, you can do this:

<http://example.com/>
Markdown will turn this into:

<a href="http://example.com/">http://example.com/</a>
Automatic links for email addresses work similarly, except that Markdown will also perform a bit of randomized decimal and hex entity-encoding to help obscure your address from address-harvesting spambots. For example, Markdown will turn this:

<address@example.com>
into something like this:

<a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
&#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
&#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>
which will render in a browser as a clickable link to “address@example.com”.

(This sort of entity-encoding trick will indeed fool many, if not most, address-harvesting bots, but it definitely won’t fool all of them. It’s better than nothing, but an address published in this way will probably eventually start receiving spam.)

#### BACKSLASH ESCAPES

Markdown allows you to use backslash escapes to generate literal characters which would otherwise have special meaning in Markdown’s formatting syntax. For example, if you wanted to surround a word with literal asterisks (instead of an HTML <em> tag), you can use backslashes before the asterisks, like this:

\*literal asterisks\*
Markdown provides backslash escapes for the following characters:

\   backslash
`   backtick
*   asterisk
_   underscore
{}  curly braces
[]  square brackets
()  parentheses
#   hash mark
+   plus sign
-   minus sign (hyphen)
.   dot
!   exclamation mark
