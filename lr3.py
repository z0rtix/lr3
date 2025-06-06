import math
import random

class Qubit:
    def __init__(self, alpha=1.0, beta=0.0):
        # Нормализуем состояние кубита
        norm = math.sqrt(abs(alpha)**2 + abs(beta)**2)
        self.alpha = alpha / norm
        self.beta = beta / norm

    def __str__(self):
        # Красиво печатаем состояние
        return f"[{self.alpha:.3f}|0⟩ + {self.beta:.3f}|1⟩]"

    def measure(self):
        # Измеряем кубит
        return 0 if random.random() < abs(self.alpha)**2 else 1

# Гейт Паули X (NOT)
def apply_x(qubit):
    # Меняем местами амплитуды
    return Qubit(qubit.beta, qubit.alpha)

# Гейт Паули Y 
def apply_y(qubit):
    # Добавляем фазу и меняем местами
    return Qubit(-qubit.beta, qubit.alpha)

# Гейт Паули Z
def apply_z(qubit):
    # Инвертируем фазу |1>
    return Qubit(qubit.alpha, -qubit.beta)

# Контролируемый NOT (CNOT)
def apply_cnot(control, target):
    # Если control= 1, применяем X к target
    if control.measure() == 1:
        return (control, apply_x(target))
    return (control, target)

# Тестируем
if __name__ == "__main__":
    # Проверка X гейта
    print("Тест X-гейта:")
    q = Qubit(1, 0)
    print(f"До: {q}")
    q = apply_x(q)
    print(f"После: {q}")

    # Проверка CNOT
    print("\nТест CNOT:")
    control = Qubit(1, 0)
    target = Qubit(1, 0)
    
    # Случай 1: control=|0>
    print("control=|0>, target=|0>")
    _, target_res = apply_cnot(control, target)
    print(f"Результат: {target_res}")
    
    # Случай 2: control=|1>
    control = apply_x(control)
    print("\ncontrol=|1>, target=|0>")
    _, target_res = apply_cnot(control, Qubit(1, 0))
    print(f"Результат: {target_res}")