from collections import OrderedDict
from typing import Optional


def analyse(programm: list[tuple[str, int, Optional[str]]]) -> int:
    minimal_quantity = 0  # минимальное количество энергии, которое будет потрачено на выполнение программы
    warehouse = OrderedDict()  # здесь будут хранится ящики после поступления на склад
    """временное хранилище для ящиков, которые потребовалось выгрузить, чтобы выгрузить нужный ящик со склада"""
    temp_warehouse = OrderedDict()

    for tuple_ in programm:
        if len(tuple_) == 3:
            command, box, optional_value = tuple_

            if command == 'принять' and optional_value == 'загрузить на вход':
                warehouse.update({box: {'command': command, 'optional_value': optional_value}})
                warehouse.move_to_end(box, last=False)
                minimal_quantity += 1
            elif command == 'принять' and optional_value == 'загрузить на выход':
                warehouse.update({box: {'command': command, 'optional_value': optional_value}})
                warehouse.move_to_end(box, last=True)
                minimal_quantity += 1
        else:
            command, box = tuple_
            if command == 'выгрузить':
                quantity_of_boxes = len(warehouse)  # количество, хранимых на складе ящиков на текущий момент
                if quantity_of_boxes == 1:
                    warehouse.pop(box)
                    minimal_quantity += 2 * 0 + 1
                else:
                    """начальный номер ящика, с которого нужно будет начать выгрузку, чтобы в последствии выгрузить 
                    нужный ящик со склада"""
                    beginning_relief_box = 0
                    for box_, params in warehouse.items():
                        beginning_relief_box += 1
                        if box_ == box:
                            break

                    """количество ящиков, которые нужно выгрузить для того, чтобы достать нужный ящик для выгрузки 
                    со склада"""
                    quantity_of_boxes_to_relieve = 0
                    quantity_of_boxes_in_warehouse = len(warehouse)  # текущее количество ящиков на складе
                    for _ in range(beginning_relief_box, quantity_of_boxes_in_warehouse):
                        relieve_box, params = warehouse.popitem(last=True)
                        quantity_of_boxes_to_relieve += 1
                        temp_warehouse.update({relieve_box: params})

                    """необходимо проитерироваться по OrderDict, имеющему обратный порядок, для восстановления 
                    предыдущего OrderDict, за исключением выгруженного ящика"""
                    for relieve_box, params in OrderedDict(list(temp_warehouse.items())[::-1]).items():
                        warehouse.update({relieve_box: params})
                        warehouse.move_to_end(relieve_box, last=True)
                    minimal_quantity += 2 * quantity_of_boxes_to_relieve + 1

    return minimal_quantity