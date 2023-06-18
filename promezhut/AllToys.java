package promezhut;

import lombok.Data;

import java.util.ArrayList;
import java.util.List;


@Data
public class AllToys implements Searchable{
     private List<Toys> allToys ;

    @Override
    public List<Toys> findToysByName(String name) {
        List<Toys> seaerchResalt = new ArrayList<>();
        for (Toys b: allToys) {
            if(b.getName().equals(name)){
                seaerchResalt.add(b);
            }

        }
        return seaerchResalt;
    }

    public void setToys(Toys toys){
        allToys.add(toys);
    }
}
