import matplotlib.pyplot as plt
import adjustText
import plotly.graph_objects as go
import tkinter as tk
from tkinter import messagebox
stars = {
    &#39;Polaris&#39;: (2.52,89.26),
    &#39;Sirius&#39;: (6.75,-16.72),
    &#39;Vega&#39;: (18.62,38.78),
    &#39;Betelgeuse&#39;: (5.92,7.41),
    &#39;Meissa&#39;:(5.58,9.93),
    &#39;Rigel&#39;:(5.24,-8.20),
    &#39;Altair&#39;:(19.85,8.87),
    &#39;Deneb&#39;:(20.69,45.28),
    &#39;Procyon&#39;:(7.66,5.22),
    &#39;Capella&#39;:(5.28,46.00),
    &#39;Arcturus&#39;:(14.26,19.18),
    &#39;Spica&#39;:(13.42,-11.16),
    &#39;Antares&#39;:(16.49,-26.43),
    &#39;Fomalhaut&#39;:(22.69,-29.62),
    &#39;Regulus&#39;:(10.14,11.97),
    &#39;Sadr&#39;:(20.22,40.26),
    &#39;Albireo&#39;:(19.51,27.96),
    &#39;Gienah&#39;:(20.77,33.97),
    &#39;Aldebaran&#39;:(4.60,16.52),
    &#39;Pollux&#39;:(7.76,28.03),
    &#39;Castor&#39;:(7.58,31.89),
    &#39;Bellatrix&#39;:(5.42,6.35),
    &#39;Alnilam&#39;:(5.60,-1.20),
    &#39;Mirach&#39;:(1.16,35.62),
    &#39;Sheliak&#39;:(18.84,33.36),
    &#39;Sulafat&#39;:(18.90,32.69),
    &#39;Algol&#39;:(3.14,40.96),
    &#39;Dubhe&#39;:(11.03,61.75),
    &#39;Merak&#39;:(11.01,56.38),
    &#39;Phecda&#39;:(11.90,53.69),
    &#39;Megrez&#39;:(12.25,57.03),
    &#39;Shaula&#39;:(17.56,-37.10),
    &#39;Sargas&#39;:(17.62,-42.99),
    &#39;Dschubba&#39;:(16.00,-22.62),
    &quot;Denebola&quot;:(11.82,14.57),
    &quot;Algieba&quot;:(10.33,19.84),
    &#39;Alhena&#39;:(6.63,16.40),
    &#39;Wasat&#39;:(7.35,21.98),
    &#39;Elnath&#39;:(5.44,28.61),
    &#39;Pleione&#39;:(3.82,24.18),
    &#39;Schedar&#39;:(0.68,56.54),
    &#39;Caph&#39;:(0.15,59.15),
    &quot;Gamma cas&quot;:(0.95,60.72),
    &#39;Alioth&#39;:(12.88,55.96),
    &#39;Mizar&#39;:(13.40,54.92),
    &#39;Alkaid&#39;:(13.79,49.31),
    &#39;Saiph&#39;:(5.80,-9.67),
    &#39;Mintaka&#39;:(5.53,-0.3),
    &#39;Yildun&#39;:(17.54,86.59),
    &#39;Kochab&#39;: (14.85, 74.15),
    &#39;Pherkad&#39;: (15.74, 71.83),
    &#39;Alnitak&#39;: (5.68, -1.94),
    &#39;Epsilon UMi&#39;: (16.77, 82.03),
    &#39;Zeta UMi&#39;: (15.74, 77.80),
    &#39;Eta UMi&#39;: (16.29, 75.76),
    &#39;Segin&#39;: (1.90, 63.67),
    &#39;Ruchbah&#39;: (1.43, 60.24),
    &#39;Adhafera&#39;:(10.27,23.42),
    &#39;Ras Elased Australis&#39;:(9.76,23.77),
    &#39;Ras Elased Borealis&#39;:(9.47,26.01),
    &#39;Zosma&#39;:(11.23,20.52),
    &#39;Chort&#39;:(11.24,15.43),

    }
constellations={
   
&quot;Orion&quot;:[&#39;Mintaka&#39;,&#39;Alnilam&#39;,&#39;Alnitak&#39;,&#39;Saiph&#39;,&#39;Rigel&#39;,&#39;Mintaka&#39;,&#39;Bellatrix&#39;,&#39;Meissa&#39;,&#39;Betelgeuse&#39;,&#39;Alnit
ak&#39;],
    &quot;Ursa Major&quot;:[&quot;Alkaid&quot;,&quot;Mizar&quot;,&quot;Alioth&quot;,&quot;Megrez&quot;,&quot;Phecda&quot;,&quot;Merak&quot;,&quot;Dubhe&quot;,&quot;Megrez&quot;],
    &quot;Ursa Minor&quot;:[&#39;Polaris&#39;, &#39;Yildun&#39;, &#39;Epsilon UMi&#39;, &#39;Zeta UMi&#39;,&#39;Eta UMi&#39;, &#39;Pherkad&#39;, &#39;Kochab&#39;,
&#39;Polaris&#39;],
    &quot;Cassiopeia&quot;:[&quot;Segin&quot;,&quot;Ruchbah&quot;,&quot;Gamma cas&quot;,&quot;Schedar&quot;,&quot;Caph&quot;],
    &quot;Leo&quot;:[&#39;Regulus&#39;, &#39;Algieba&#39;, &#39;Adhafera&#39;, &#39;Ras Elased Australis&#39;, &#39;Ras Elased Borealis&#39;, &#39;Zosma&#39;,
&#39;Chort&#39;],
    &quot;Taurus&quot;: [&#39;Aldebaran&#39;, &#39;Elnath&#39;, &#39;Pleione&#39;],
    &quot;Gemini&quot;: [&#39;Pollux&#39;, &#39;Castor&#39;, &#39;Wasat&#39;, &#39;Alhena&#39;],
    &quot;Scorpius&quot;: [&#39;Dschubba&#39;, &#39;Antares&#39;, &#39;Shaula&#39;, &#39;Sargas&#39;],
    &quot;Cygnus&quot;: [&#39;Deneb&#39;, &#39;Sadr&#39;, &#39;Albireo&#39;, &#39;Gienah&#39;],
    &quot;Lyra&quot;: [&#39;Vega&#39;, &#39;Sheliak&#39;, &#39;Sulafat&#39;]
    }
def load_constellation_info(filepath=&quot;constellation_data.txt&quot;):
    data = {}
    with open(filepath, &#39;r&#39;) as f:
        lines = f.readlines()
    current = None
    for line in lines:
        line = line.strip()
        if line.startswith(&quot;[&quot;) and line.endswith(&quot;]&quot;):
            current = line[1:-1]
            data[current] = {}
        elif &quot;Alias:&quot; in line:
            data[current][&quot;alias&quot;] = line.split(&quot;Alias:&quot;)[1].strip()
        elif &quot;Major Stars:&quot; in line:
            stars_line = line.split(&quot;Major Stars:&quot;)[1].strip()
            data[current][&quot;major_stars&quot;] = [s.strip() for s in stars_line.split(&#39;,&#39;)]
        elif &quot;Fact:&quot; in line:
            data[current][&quot;fact&quot;] = line.split(&quot;Fact:&quot;)[1].strip()
    return data
def constellation_map():  
    text=[]
    plt.figure(figsize=(25,25))
    ax=plt.axes(facecolor=&#39;black&#39;)
    for name, (x, y) in stars.items():
        plt.scatter(x, y, color=&#39;white&#39;)
        ax.annotate(
            name,
            (x, y),
            textcoords=&quot;offset points&quot;,
            xytext=(5, 5),  # Arrow offset
            ha=&#39;center&#39;,
            color=&#39;cyan&#39;,
            fontsize=10,
            arrowprops=dict(arrowstyle=&quot;-&gt;&quot;, color=&#39;gray&#39;, shrinkA=10)
        )
    ax.set_xlim(0,25)
    ax.set_ylim(-50,95)
    plt.grid(linestyle=&#39;dashed&#39;)
    plt.title(&quot;2D Star map&quot;)
    plt.xlabel(&quot;Right Acession[RA] in hrs&quot;)
    plt.ylabel(&quot;Deg°&quot;)
    orion_order = [&#39;Betelgeuse&#39;, &#39;Bellatrix&#39;, &#39;Mintaka&#39;, &#39;Alnilam&#39;, &#39;Rigel&#39;, &#39;Saiph&#39;, &#39;Betelgeuse&#39;]
    x_vals = [stars[star][0] for star in orion_order]
    y_vals = [stars[star][1] for star in orion_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)

    plt.text(7.07,-1.4, &#39;Orion&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
    ursamajor_order = [&#39;Dubhe&#39;, &#39;Merak&#39;, &#39;Phecda&#39;, &#39;Megrez&#39;, &#39;Alioth&#39;, &#39;Mizar&#39;, &#39;Alkaid&#39;,&#39;Dubhe&#39;]
    x_vals = [stars[star][0] for star in ursamajor_order]
    y_vals = [stars[star][1] for star in ursamajor_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(12.62,64.6, &#39;Ursa Major&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
   
    cygnus_order = [&#39;Deneb&#39;, &#39;Sadr&#39;, &#39;Albireo&#39;, &#39;Gienah&#39;, &#39;Deneb&#39;]
    x_vals = [stars[star][0] for star in cygnus_order]
    y_vals = [stars[star][1] for star in cygnus_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(21,22.6, &#39;Cygnus&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
    lyra_order = [&#39;Vega&#39;, &#39;Sheliak&#39;, &#39;Sulafat&#39;,&#39;Vega&#39;]
    x_vals = [stars[star][0] for star in lyra_order]
    y_vals = [stars[star][1] for star in lyra_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(17.51,34.3, &#39;Lyra&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
    scorpius_order = [&#39;Dschubba&#39;, &#39;Antares&#39;, &#39;Shaula&#39;, &#39;Sargas&#39;]
    x_vals = [stars[star][0] for star in scorpius_order]
    y_vals = [stars[star][1] for star in scorpius_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(17.91,-22.8, &#39;Scorpius&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
   
    leo_order = [&#39;Regulus&#39;, &#39;Algieba&#39;, &#39;Denebola&#39;, &#39;Regulus&#39;]
    x_vals = [stars[star][0] for star in leo_order]
    y_vals = [stars[star][1] for star in leo_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(11.74,20.9, &#39;Leo&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
   
    gemini_order = [&#39;Pollux&#39;, &#39;Castor&#39;, &#39;Wasat&#39;, &#39;Alhena&#39;, &#39;Pollux&#39;]
    x_vals = [stars[star][0] for star in gemini_order]
    y_vals = [stars[star][1] for star in gemini_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(7.90,38.7, &#39;Gemini&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
   
    taurus_order = [&#39;Aldebaran&#39;, &#39;Elnath&#39;, &#39;Pleione&#39;, &#39;Aldebaran&#39;]
    x_vals = [stars[star][0] for star in taurus_order]
    y_vals = [stars[star][1] for star in taurus_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(1.80,20.5, &#39;Taurus&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
   
    cass_order = [&#39;Schedar&#39;,&#39;Caph&#39;,&#39;Gamma cas&#39;,&#39;Schedar&#39;]
    x_vals = [stars[star][0] for star in cass_order]
    y_vals = [stars[star][1] for star in cass_order]
    plt.plot(x_vals, y_vals, color=&#39;yellow&#39;, linewidth=1.5,zorder=1)
    plt.text(1.22,67.1, &#39;Cassiopeia&#39;, color=&#39;orange&#39;, fontsize=14, fontweight=&#39;bold&#39;)
    plt.show()

def constellation_info(stars,constellations,s):
    info_data = load_constellation_info()
    if s not in constellations:
        print(&quot;Please select a constellation from the above list only.&quot;)
    fig=go.Figure()
    star_list=constellations[s]
    stars_used={name:stars[name] for name in star_list if name in stars}
    for name,(x,y) in stars_used.items():
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode=&#39;markers+text&#39;,
            name=name,
            text=[name],
            textposition=&#39;top center&#39;,
            marker=dict(color=&#39;white&#39;, size=8),
            hovertemplate=f&quot;&lt;b&gt;{name}&lt;/b&gt;&lt;br&gt;RA: {x} hrs&lt;br&gt;Dec: {y}°&lt;extra&gt;&lt;/extra&gt;&quot;
        ))
    x_vals = [stars[star][0] for star in star_list if star in stars]

    y_vals = [stars[star][1] for star in star_list if star in stars]
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals,
        mode=&#39;lines&#39;,
        name=s,
        line=dict(color=&#39;yellow&#39;, width=2),
        hoverinfo=&#39;skip&#39;
    ))
    cx = sum(x_vals) / len(x_vals)
    cy = sum(y_vals) / len(y_vals)
    fig.add_trace(go.Scatter(
        x=[cx], y=[cy],
        mode=&#39;text&#39;,
        text=[s],
        textposition=&#39;top center&#39;,
        textfont=dict(color=&#39;orange&#39;, size=14)
    ))
    fig.update_layout(
        title=f&quot;{s} Constellation&quot;,
        xaxis=dict(title=&#39;Right Ascension (hrs)&#39;, range=[min(x_vals)-1, max(x_vals)+1],
showgrid=True,zeroline=False, gridcolor=&#39;gray&#39;),
        yaxis=dict(title=&#39;Declination (°)&#39;, range=[min(y_vals)-10, max(y_vals)+10],
showgrid=True,zeroline=False, gridcolor=&#39;gray&#39;),
        paper_bgcolor=&#39;black&#39;,
        plot_bgcolor=&#39;black&#39;,
        font=dict(color=&#39;cyan&#39;),
        showlegend=False
    )
    fig.show()
   
    print(&quot;\n--- CONSTELLATION INFO ---&quot;)
    print(f&quot;Name       : {s}&quot;)
    print(f&quot;Alias      : {info_data[s][&#39;alias&#39;]}&quot;)
    print(f&quot;Major Stars: {&#39;, &#39;.join(info_data[s][&#39;major_stars&#39;])}&quot;)
    print(f&quot;Fact       : {info_data[s][&#39;fact&#39;]}\n&quot;)
def constellation_quiz():
    quiz_data = [
        {
            &#39;question&#39;: &quot;Which constellation is known as the &#39;Hunter&#39;?&quot;,
            &#39;options&#39;: [&#39;Orion&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Cassiopeia&#39;],
            &#39;answer&#39;: &#39;Orion&#39;
        },
        {
            &#39;question&#39;: &quot;The North Star is located in which constellation?&quot;,
            &#39;options&#39;: [&#39;Orion&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Cassiopeia&#39;],
            &#39;answer&#39;: &#39;Ursa Minor&#39;
        },
        {
            &#39;question&#39;: &quot;Which constellation is famous for its &#39;W&#39; shape?&quot;,
            &#39;options&#39;: [&#39;Orion&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Cassiopeia&#39;],
            &#39;answer&#39;: &#39;Cassiopeia&#39;
        },
        {
            &#39;question&#39;: &quot;Which constellation contains the star Betelgeuse?&quot;,
            &#39;options&#39;: [&#39;Orion&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Cassiopeia&#39;],
            &#39;answer&#39;: &#39;Orion&#39;
        },
        {
            &#39;question&#39;: &quot;Which of these is NOT a zodiac constellation?&quot;,
            &#39;options&#39;: [&#39;Leo&#39;, &#39;Scorpius&#39;, &#39;Pegasus&#39;, &#39;Taurus&#39;],
            &#39;answer&#39;: &#39;Pegasus&#39;
        },
        {
            &#39;question&#39;: &quot;Which shape is the constellation Lyra known for?&quot;,
            &#39;options&#39;: [&#39;Triangle&#39;, &#39;W&#39;, &#39;Harp&#39;, &#39;Circle&#39;],
            &#39;answer&#39;: &#39;Harp&#39;
        },
        {

            &#39;question&#39;: &quot;Which constellation is represented as a bull?&quot;,
            &#39;options&#39;: [&#39;Orion&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Taurus&#39;],
            &#39;answer&#39;: &#39;Taurus&#39;
        },
        {
            &#39;question&#39;: &quot;Which constellation represents a Lion?&quot;,
            &#39;options&#39;: [&#39;Leo&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Cassiopeia&#39;],
            &#39;answer&#39;: &#39;Leo&#39;
        },
        {
            &#39;question&#39;: &quot;Which constellation is visible all year around?&quot;,
            &#39;options&#39;: [&#39;Orion&#39;, &#39;Ursa Major&#39;, &#39;Ursa Minor&#39;, &#39;Cassiopeia&#39;],
            &#39;answer&#39;: &#39;Ursa Major&#39;
        },
        {
            &#39;question&#39;: &quot;Which star is located at the heart of the Scorpius Constellation?&quot;,
            &#39;options&#39;: [&#39;Vega&#39;, &#39;Antares&#39;, &#39;Sirius&#39;, &#39;Polaris&#39;],
            &#39;answer&#39;: &#39;Antares&#39;
        }
    ]
    root = tk.Tk()
    root.title(&quot;Constellation Quiz&quot;)
    root.geometry(&quot;500x350&quot;)
   
    question_index = [0]
    score = [0]
    def load_question():
        answer_var.set(None)
        q = quiz_data[question_index[0]]
        question_label.config(text=f&quot;Q{question_index[0]+1}: {q[&#39;question&#39;]}&quot;)
        for i, option in enumerate(q[&#39;options&#39;]):
            option_buttons[i].config(text=option, value=option)
        feedback_label.config(text=&quot;&quot;)
    def submit_answer():
        selected = answer_var.get()
        correct_answer = quiz_data[question_index[0]][&#39;answer&#39;]
        if selected == correct_answer:
            score[0] += 1
            feedback_label.config(text=&quot;Correct!&quot;, fg=&quot;green&quot;)
        else:
            feedback_label.config(text=f&quot;Wrong! Correct answer: {correct_answer}&quot;, fg=&quot;red&quot;)
        submit_btn.config(state=&quot;disabled&quot;)
        next_btn.config(state=&quot;normal&quot;)
    def next_question():
        question_index[0] += 1
        if question_index[0] &lt; len(quiz_data):
            load_question()
            submit_btn.config(state=&quot;normal&quot;)
            next_btn.config(state=&quot;disabled&quot;)
        else:
            messagebox.showinfo(&quot;Quiz Finished&quot;, f&quot;You scored {score[0]} out of {len(quiz_data)}&quot;)
            root.destroy()
    question_label = tk.Label(root, text=&quot;&quot;, wraplength=450, font=(&quot;Helvetica&quot;, 12))
    question_label.pack(pady=20)
    answer_var = tk.StringVar()
    option_buttons = []
    for _ in range(4):
        btn = tk.Radiobutton(root, text=&quot;&quot;, variable=answer_var, value=&quot;&quot;, font=(&quot;Helvetica&quot;, 10))
        btn.pack(anchor=&quot;w&quot;, padx=40)
        option_buttons.append(btn)
    feedback_label = tk.Label(root, text=&quot;&quot;, font=(&quot;Helvetica&quot;, 10))
    feedback_label.pack(pady=5)
    submit_btn = tk.Button(root, text=&quot;Submit&quot;, command=submit_answer)
    submit_btn.pack(pady=5)

    next_btn = tk.Button(root, text=&quot;Next&quot;, command=next_question, state=&quot;disabled&quot;)
    next_btn.pack(pady=5)
    load_question()
    root.mainloop()
# Main program
print(&quot;          ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗           \n          ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║      
    \n          ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝           \n          ╦╔╗╔╔╦╗╔═╗╦═╗╔═╗╔═╗╔╦╗╦╦  ╦╔═╗      
   \n          ║║║║ ║ ║╣ ╠╦╝╠═╣║   ║ ║╚╗╔╝║╣           \n          ╩╝╚╝ ╩ ╚═╝╩╚═╩ ╩╚═╝ ╩ ╩ ╚╝ ╚═╝        
 \n  ╔═╗╔═╗╔╗╔╔═╗╔╦╗╔═╗╦  ╦  ╔═╗╔╦╗╦╔═╗╔╗╔  ╔╦╗╔═╗╔═╗\n  ║  ║ ║║║║╚═╗ ║ ║╣ ║  ║  ╠═╣ ║ ║║ ║║║║
 ║║║╠═╣╠═╝\n  ╚═╝╚═╝╝╚╝╚═╝ ╩ ╚═╝╩═╝╩═╝╩ ╩ ╩ ╩╚═╝╝╚╝  ╩ ╩╩ ╩╩  \n              ╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗      
        \n              ╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║               \n              ╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩        
      \n&quot;)
info_data = load_constellation_info()
while True:
    print(&quot;\nPick one to continue:&quot;)
    print(&quot;1. Basic 2D star map.&quot;)
    print(&quot;2. Know about major constellations.&quot;)
    print(&quot;3. Test your knowledge on constellations.&quot;)
    print(&quot;4. Exit&quot;)
    try:
        n = int(input(&quot;Enter your choice: &quot;))
    except ValueError:
        print(&quot;Invalid input. Please enter a number between 1 and 4.&quot;)
        continue
    if n == 1:
        constellation_map()
    elif n == 2:
        print(&quot;\nSome of the major constellations are:&quot;)
        for i, name in enumerate(constellations.keys(), 1):
            print(f&quot;{i}. {name}&quot;)
        s = input(&quot;Enter a constellation to continue: &quot;).strip().title()
        if s in constellations:
            constellation_info(stars, constellations, s)
        else:
            print(&quot;Constellation not found. Please check spelling.&quot;)
    elif n == 3:
        constellation_quiz()
    elif n == 4:
        print(&quot;╔═╗═╗ ╦╦╔╦╗╦╔╗╔╔═╗    ╔═╗╔═╗╔═╗╔╦╗╔╗ ╦ ╦╔═╗  \n║╣ ╔╩╦╝║ ║ ║║║║║ ╦    ║ ╦║ ║║ ║ ║║╠╩╗╚╦╝║╣
  \n╚═╝╩ ╚═╩ ╩ ╩╝╚╝╚═╝    ╚═╝╚═╝╚═╝═╩╝╚═╝ ╩ ╚═╝  \n&quot;)
        break
    else:
        print(&quot;Invalid choice. Please choose a number between 1 and 4.&quot;)
