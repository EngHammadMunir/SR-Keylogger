using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace School
{
    public partial class Roles : sample2
    {
        public Roles()
        {
            InitializeComponent();
        }
        int edit = 0;
        myDBDataContext OBJ = new myDBDataContext();
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void RoletextBox_TextChanged(object sender, EventArgs e)
        {
            if (Roletext.Text == "") { RoleErrorlabel.Visible = true; } else { RoleErrorlabel.Visible = false; }
        }

        private void StatusDD_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (StatusDD.SelectedIndex == -1) { statuserrorlabel.Visible = true; } else { statuserrorlabel.Visible = false; }
        }
        public override void addbutton_Click(object sender, EventArgs e)
        {
            edit = 0;
            MainClass.enable_reset(panel5);
        }

        public override void editbutton_Click(object sender, EventArgs e)
        {
            edit = 1;
            MainClass.enable(panel5);
        }

        public override void savebutton_Click(object sender, EventArgs e)
        {
            if (Roletext.Text == "") { RoleErrorlabel.Visible = true; } else { RoleErrorlabel.Visible = false; }
            if (StatusDD.SelectedIndex == -1) { statuserrorlabel.Visible = true; } else { statuserrorlabel.Visible = false; }
            if(RoleErrorlabel.Visible||statuserrorlabel.Visible)
            {
                MainClass.showMsg("Field With * Are Important For Save", "Error", "Error");
            }
            else
            {
                if(edit==0) //code for save opp
                {
                    role r = new role();
                    r.r_name = Roletext.Text;
                    if(StatusDD.SelectedIndex==0)
                    {
                        r.r_status = 1;
                    }
                    else
                    {
                        r.r_status = 0;
                    }
                    OBJ.st_insertRoles(Roletext.Text, r.r_status);
                    OBJ.SubmitChanges();
                    MainClass.showMsg(Roletext.Text + " Added Successfully in The System", "Success", "Success");
                    MainClass.disable_reset(panel5);
                    loaddata();
                }
                else if(edit ==1) //code for update 
                {
                    var data = OBJ.roles.Single(x => x.r_id == roleID);
                    data.r_name = Roletext.Text;
                    if (StatusDD.SelectedIndex == 0)
                    {
                        data.r_status = 1;
                    }
                    else
                    {
                        data.r_status = 0;
                    }
                    OBJ.SubmitChanges();
                    MainClass.showMsg(Roletext.Text + " Updated Successfully in The System", "Success", "Success");
                    MainClass.disable_reset(panel5);
                    loaddata();
                }
            }
        }

        public override void deletebutton_Click(object sender, EventArgs e)
        {

        }
        public void loaddata()
        { 
            MainClass.disable_reset(panel5);
            var abc = OBJ.st_getRoles();              // show Data On Grid View
            roleIDGV.DataPropertyName = "ID";      // show Data On Grid View
            RoleGV.DataPropertyName = "Role";       // show Data On Grid View
            StatusGV.DataPropertyName = "Status";     // show Data On Grid View
            dataGridView1.DataSource = abc;     // show Data On Grid View
            MainClass.sno(dataGridView1, "snoGV");
        }
    public override void viewbutton_Click(object sender, EventArgs e)
        {
            loaddata();
        }

        public override void searchtextBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void Roles_Load(object sender, EventArgs e)
        {
        }
        int roleID;
        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if(e.RowIndex !=-1 && e.ColumnIndex!=-1)
            {
                DataGridViewRow row = dataGridView1.Rows[e.RowIndex];
                roleID = Convert.ToInt32(row.Cells["roleIDGV"].Value.ToString());
                
            }
        }
    }
}
