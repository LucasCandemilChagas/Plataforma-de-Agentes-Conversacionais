# Plataforma de Agentes Conversacionais com Infraestrutura de Microsserviços

Uma plataforma escalável, resiliente e observável para orquestração e execução de agentes de Inteligência Artificial Conversacionais. Projetada para funcionar perfeitamente em ambientes de desenvolvimento local (sem dependência de recursos de nuvem) e em clusters Kubernetes em ambiente de produção.

---

## Visão Geral

O projeto tem como propósito projetar e implementar a infraestrutura necessária para suportar a execução de **Agentes de IA** baseados no ciclo contínuo de **Raciocínio → Ação → Observação**:

1. **Raciocínio:** O agente recebe a requisição do usuário e processa a lógica de solução através de um Modelo de Linguagem (LLM).
2. **Ação:** O agente pode invocar ferramentas externas para obter dados adicionais ou executar ações no sistema.
3. **Observação:** O agente analisa os resultados obtidos das ferramentas chamadas.
4. **Iteração:** O ciclo se repete continuadamente até que o agente produza a resposta final.

A plataforma garante que todo esse fluxo ocorra de maneira resiliente, escalável e com gerenciamento eficiente de memória de conversação e roteamento de requisições.

---

## Arquitetura e Microsserviços

A plataforma é composta por microsserviços independentes e desacoplados, cobrindo as seguintes responsabilidades:

* **Roteamento & Entrada (API Gateway):** Gerencia o tráfego de entrada e faz o roteamento das requisições para os serviços correspondentes.
* **Orquestrador de Agentes (*Agent Orchestrator*):** Gerencia a execução do ciclo *Raciocínio → Ação → Observação* e coordena a interação com os LLMs.
* **Gerenciador de Memória (*Memory Service*):** Responsável pela retenção e recuperação do contexto e histórico de conversas dos agentes.
* **Executor de Ferramentas (*Tools Service*):** Provê as integrações com APIs e sistemas externos chamados pelos agentes durante a fase de Ação.
* **Observabilidade & Resiliência:** Camada para rastreamento (*tracing*), métricas e mecanismos de tolerância a falhas na comunicação entre microsserviços.

---

## Ambientes de Execução

A plataforma oferece portabilidade total entre os ambientes através de contêineres:

### 1. Desenvolvimento Local (`Docker Compose`)
* **100% Autônomo:** Não possui dependência de serviços ou recursos em nuvem para rodar a infraestrutura base.
* Ideal para desenvolvimento, testes de integração e iteração rápida.

### 2. Produção (`Kubernetes`)
* Implantação preparada para clusters Kubernetes gerenciados ou *on-premise*.
* Suporte a escalabilidade horizontal automática (HPA), alta disponibilidade e tolerância a falhas.

---

## 💻 Como Executar

### Pré-requisitos
* [Git](https://git-scm.com/)
* [Docker Engine](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/) *(necessário apenas para deploy em Kubernetes)*
