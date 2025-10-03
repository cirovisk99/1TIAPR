
// Pinos dos botões e do LED
const int botao1 = 32;   // Botão 1 no pino digital 32
const int botao2 = 33;   // Botão 2 no pino digital 33
const int botao3 = 34;   // Botão 3 no pino digital 34
const int led1 = 21;     // LED no pino digital
const int led2 = 22;     // LED no pino digital
const int led3 = 23;     // LED no pino digital

void setup() {
  pinMode(botao1, INPUT_PULLUP); // Usa resistor interno de pull-up
  pinMode(botao2, INPUT_PULLUP);
  pinMode(botao3, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

  
void loop() {
  // Leitura dos botões (LOW = pressionado por causa do pull-up)
  bool estadoBotao1 = digitalRead(botao1);
  bool estadoBotao2 = digitalRead(botao2);
  bool estadoBotao3 = digitalRead(botao3);

  // Usa operador AND: LED só acende se os dois forem pressionados
  if (!estadoBotao1 && !estadoBotao2) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led3, LOW);
  }

  delay(100);
}

