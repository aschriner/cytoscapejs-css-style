'''
Parses a CSS stylesheet into the funky JSON format demanded by Cytoscape.js.
Generates a file called "cytoscapestyle.json" which can be loaded by 
Cytoscape.js.

See README for more info.  
'''

import tinycss
import json

def main():
    cssfile = "cytoscape.css"
    parser = tinycss.make_parser('page3')
    with open(cssfile, "r") as f:
        stylesheet = parser.parse_stylesheet_file(f)
        out = []
        #loop over css rules and generate JSON 
        for rule in stylesheet.rules:
            declarations = {}
            if rule.declarations: #ignore if nothing is declared for selector
                for d in rule.declarations:
                    declarations[d.name] = d.value.as_css()
                dict = {"css": declarations,
                        "selector": rule.selector.as_css() }
                out.append(dict)
    
    #Write to json file
    jsonfile = "cytoscapestyle.json"
    with open(jsonfile, "wb") as j:    
        json.dump(out, j)


if __name__ == "__main__":
    main()
