import PySimpleGUI as sg

def gui_launch():
        
    layout = [ 
            [sg.Button("Adress")],
            [sg.Text("Adress: ", size=(30, 2), text_color="black", key="fest_adress")],
            [sg.Button("Alkohol")],
            [sg.Text("Alkohol: ", size=(12,3), text_color="black", key="fest_alkohol")],
            [sg.Button("Välj plats på kartan")],
            [sg.Text("pos: ", size=(5,5), text_color="black", key="coords")],
            [sg.Button("Submit")],
            [sg.Text(size=(8,1), text_color="red", key='-DISPLAY-')  ],
            [sg.Button("distance threshold")],
            [sg.Text(size=(10,1), text_color = "red", key = "far_away") ],
            [sg.Graph((800, 800), (0, 450), (450, 0), key ="-GRAPH-", drag_submits=True, enable_events=True)]
            
    ]
    window = sg.Window("planerare", layout = layout, background_color ="#272533", size=(500,500),return_keyboard_events=True)
    graph = window["-GRAPH-"]
    fest_ids = []
    alk_amounts = []
    fest_pos = []
    maximum_dist = 0
    while True:
        
        event, values = window.read()
        if event is None:
            break

        if event in ["Adress"]:
            fest_name = ""
            while True:
                ev2, val2 = window.read()
                if ev2 in ["Submit"]:
                    fest_ids.append([fest_name])
                    break

                else:
                    fest_name += ev2
                    window['fest_adress'].update(value=fest_name)
            window['fest_adress'].update(value=fest_name)

        elif event in ["Alkohol"]:
            alk_num = ""
            while True:
                ev4, val4 = window.read()
                
                if ev4 is None:
                    break

                if ev4 in ["Submit"]:
                    alk_amounts.append(alk_num)
                    break

                else:
                    alk_num += ev4
                    window['fest_alkohol'].update(value=str(alk_num))
            window['fest_alkohol'].update(value=str(alk_num))

        elif event in ["Välj plats på kartan"]:
            while True:
                ev7, val7 = window.read()
                mouse = val7['-GRAPH-']
                window["-GRAPH-"].draw_point(mouse, 10, color='green')
                #window['_DISPLAY_'].update(mouse)
                prior_rect = graph.draw_circle((mouse[0], mouse[1]), 5, line_color='red')
                window['-DISPLAY-'].update(value=str(mouse))

                if ev7 is None:
                    break

                if ev7 in ["Submit"]:
                    fest_pos.append((mouse[0], mouse[1]))
                    break

        elif event in ["distance threshold"]:
            max_dist = ""
            while True:
                ev9, val9 = window.read()
                
                if ev9 is None:
                    break

                if ev9 in ["Submit"]:
                    maximum_dist = int(max_dist)
                    break

                else:
                    max_dist += ev9
                    window['far_away'].update(value=str(max_dist))
            window['far_away'].update(value=str(max_dist))


    tot_info = [[i, j, k] for i, j, k in zip(fest_ids, alk_amounts, fest_pos)]

    fester = {}
    for place in tot_info:
        name = place[0][0]
        drinks = int(place[1])
        coords = place[2]
        fester[name] = {"pos": coords, "alkohol": drinks}
        
    return fester, int(max_dist)
